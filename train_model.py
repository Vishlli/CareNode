import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score
import os
import sys
# Configuration
DATASET_PATH = "cattle_health_data.csv"
MODEL_PATH = "model.tflite"
# 1. Load Dataset
print(f"Status: Loading dataset from {DATASET_PATH}...")
if not os.path.exists(DATASET_PATH):
    print(f"❌ ERROR: File '{DATASET_PATH}' not found!")
    print("Please create a CSV with columns: [temperature, breathing_rate, audio_rms, zcr, label]")
    print("Example row: 38.5, 25, 0.05, 10, 0")
    sys.exit(1)
try:
    df = pd.read_csv(DATASET_PATH)
    # Expected columns: temperature, breathing_rate, audio_rms, zcr, label
    feature_cols = ['temperature', 'breathing_rate', 'audio_rms', 'zcr']
    
    if 'label' not in df.columns:
        raise ValueError("CSV must contain a 'label' column (0=Normal, 1=Monitor, 2=Critical).")
        
    X = df[feature_cols].values
    y = df['label'].values
    
    print(f"✅ Loaded {len(df)} samples.")
    
except Exception as e:
    print(f"❌ ERROR loading CSV: {e}")
    sys.exit(1)
# 2. Preprocessing
print("Status: Normalizing data...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Print Mean and Std for ESP32 implementation
print("\n=== ESP32 NORMALIZATION CONSTANTS ===")
print("Copy these values to your C++ sketch for the ESP32:")
print(f"MEAN: {{ {', '.join([f'{x:.4f}' for x in scaler.mean_])} }}")
print(f"STD:  {{ {', '.join([f'{x:.4f}' for x in scaler.scale_])} }}")
print("=====================================\n")
# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
# 3. Model Architecture (TinyML Optimized)
# Using a small architecture to ensure < 50KB size
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(12, activation='relu'), # Reduced neurons for size
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
# 4. Train
print("Status: Training model...")
history = model.fit(X_train, y_train, epochs=50, batch_size=16, verbose=1, validation_split=0.2)
# 5. Evaluate
print("Status: Evaluating model...")
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\nModel Accuracy: {accuracy*100:.2f}%")
y_pred = np.argmax(model.predict(X_test), axis=1)
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)
# 6. Export to TFLite (Quantized)
print("\nStatus: Converting to TFLite with quantization...")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT] # Enable default optimizations (quantization)
tflite_model = converter.convert()
with open(MODEL_PATH, "wb") as f:
    f.write(tflite_model)
size_kb = os.path.getsize(MODEL_PATH) / 1024
print(f"\nSuccess! Model saved to {MODEL_PATH}")
print(f"Model Size: {size_kb:.2f} KB")
if size_kb < 50:
    print("✅ PASS: Model fits within TinyML constraints (< 50 KB).")
else:
    print(f"⚠️ WARN: Model is {size_kb:.2f} KB, which exceeds the 50 KB target.")