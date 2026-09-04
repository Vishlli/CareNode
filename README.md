# CareNode

### AI-Powered Cattle Health Monitoring Kiosk

CareNode is an **AI-powered, IoT-enabled cattle health monitoring kiosk** designed to provide quick and accessible preliminary health assessment for cattle.

The system combines **embedded sensing, audio-based analysis, TinyML, and a farmer-friendly dashboard** to identify potential respiratory and health abnormalities without requiring continuous manual observation.

> **CareNode — Early detection. Smarter monitoring. Healthier cattle.**

---

## Problem Statement

Cattle health is often monitored through periodic visual inspection, which can make it difficult to identify early symptoms of respiratory or other health-related abnormalities.

For small and medium-scale dairy farms, continuous veterinary monitoring may also be difficult due to cost and accessibility.

CareNode addresses this problem by providing a **low-cost automated health screening kiosk** that can collect cattle health data and use an embedded machine-learning model to identify abnormal patterns.

---

## Solution

CareNode acts as a **standalone cattle health screening kiosk**.

A cattle interacts with the kiosk, where sensors collect relevant health signals. The acquired data is processed locally using an **ESP32-based embedded system and TinyML model**.

The system then presents the assessment through a simple dashboard, allowing farmers or veterinary personnel to review the cattle's health status and identify animals that may require further examination.

### Core Workflow

```text
Cattle
   ↓
Sensor / Audio Data
   ↓
ESP32
   ↓
Signal Processing
   ↓
TinyML Model
   ↓
Health Classification
   ↓
Dashboard
   ↓
Farmer / Veterinarian
```

---

## Key Features

* **Cattle Health Screening**
* **Respiratory Audio Analysis**
* **TinyML-based Health Classification**
* **Edge Processing using ESP32**
* **Health Monitoring Dashboard**
* **Health Trend Visualization**
* **Veterinary Review Interface**
* **AI-generated Health Suggestions**
* **Local Dataset & Model Support**
* **Low-cost and scalable architecture**

---

## AI & Machine Learning

CareNode uses a lightweight machine-learning pipeline designed for deployment on resource-constrained embedded hardware.

### Pipeline

```text
Raw Health / Audio Data
        ↓
Preprocessing
        ↓
Feature Extraction
        ↓
ML Model Training
        ↓
Model Conversion
        ↓
TensorFlow Lite
        ↓
ESP32 Deployment
        ↓
On-device Inference
```

The repository includes:

* `train_model.py` — model training
* `convert.py` — model conversion
* `model.tflite` — TensorFlow Lite model
* `model_data.h` — embedded model representation
* `cattle_health_data.csv` — training / health dataset

---

## Hardware

The prototype is designed around an **ESP32-based embedded system**.

### Main Components

| Component                 | Purpose                             |
| ------------------------- | ----------------------------------- |
| ESP32                     | Main processing and control unit    |
| Microphone / Audio Sensor | Captures cattle respiratory sounds  |
| Sensors                   | Collect health-related measurements |
| Display / Kiosk Interface | Presents assessment results         |
| Power Supply              | Provides portable operation         |

The architecture can be extended with additional sensors depending on the health parameters being monitored.

---

## Software Stack

### Embedded

* **ESP32**
* Arduino Framework
* C/C++
* TensorFlow Lite / TinyML

### Machine Learning

* Python
* TensorFlow
* Machine Learning / Deep Learning
* Audio signal processing

### Frontend

* HTML
* CSS
* JavaScript

### Backend / API

* JavaScript
* REST-style API communication

### Data

* CSV-based cattle health dataset
* TensorFlow Lite model

---

## Project Structure

```text
CareNode/
│
├── api.js
├── cattle_health_data.csv
│
├── convert.py
├── train_model.py
│
├── model.tflite
├── model_data.h
│
├── sketch_mar26a.ino
│
├── index.html
├── styles.css
├── suggestions.html
├── trends.html
└── vet.html
```

---

## Dashboard

CareNode provides multiple interfaces for monitoring and interpreting cattle health information.

### Main Dashboard

Provides an overview of the cattle health assessment.

### Health Trends

Allows health information to be visualized over time.

### Suggestions

Provides preliminary recommendations based on the detected health condition.

### Veterinary Interface

Provides a dedicated interface for reviewing cattle health information and supporting further veterinary assessment.

---

## System Architecture

```text
                  ┌──────────────────┐
                  │      CATTLE      │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Sensors / Audio  │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │      ESP32       │
                  │ Edge Processing  │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Signal Processing│
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │   TinyML Model   │
                  │ TensorFlow Lite  │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Health Assessment│
                  └────────┬─────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │      CareNode Dashboard  │
              └────────────┬─────────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
          ┌─────────────┐     ┌─────────────┐
          │   Farmer    │     │ Veterinarian│
          └─────────────┘     └─────────────┘
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Vishlli/CareNode.git
cd CareNode
```

### 2. Machine Learning Setup

Install the required Python packages:

```bash
pip install tensorflow numpy pandas scikit-learn
```

Train the model:

```bash
python train_model.py
```

Convert the trained model for embedded deployment:

```bash
python convert.py
```

---

### 3. Run the Dashboard

Open:

```text
index.html
```

in a web browser.

---

### 4. ESP32 Setup

1. Install the Arduino IDE.
2. Add ESP32 board support.
3. Connect the ESP32 to the computer.
4. Open:

```text
sketch_mar26a.ino
```

5. Select the appropriate ESP32 board and COM port.
6. Upload the firmware.

---

## Health Assessment

CareNode is intended as a **screening and early-warning system**, not as a replacement for professional veterinary diagnosis.

A detected abnormality should be treated as an indication that the cattle may require further observation or veterinary examination.

---

## Applications

CareNode can be deployed in:

* Dairy farms
* Livestock farms
* Veterinary clinics
* Cattle shelters
* Rural livestock monitoring programs
* Agricultural research environments

---

## Future Enhancements

* Wireless synchronization between multiple kiosks
* Cloud-based cattle health records
* Dedicated farmer mobile application
* Automated abnormality alerts
* Additional physiological sensors
* Improved respiratory disease classification
* Continuous model improvement with larger datasets
* Individual cattle identification using RFID / computer vision
* Long-term health prediction
* Multi-farm centralized monitoring

---

## Impact

CareNode aims to make **early cattle health screening more accessible, affordable, and scalable**.

By combining IoT and edge AI, the system can reduce dependence on continuous manual observation and help farmers identify potentially unhealthy cattle earlier.

### Expected Benefits

* Earlier identification of health abnormalities
* Reduced manual monitoring effort
* Affordable health-screening infrastructure
* Improved access to preliminary health assessment
* Better cattle management
* Support for timely veterinary intervention

---

## ⚠️ Disclaimer

CareNode is a **prototype health-screening system** intended to assist farmers and veterinary professionals.

Its predictions should **not be considered a definitive veterinary diagnosis**. Suspected health abnormalities should be evaluated by a qualified veterinarian.

---
## ⭐ Project

If you find CareNode interesting, consider giving the repository a ⭐.

**CareNode — AI-powered cattle health monitoring through accessible edge intelligence.**
