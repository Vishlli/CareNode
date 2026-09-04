#define BUZZER 27

void setup() {
  ledcSetup(0, 2000, 8);      // channel 0, 2kHz
  ledcAttachPin(BUZZER, 0);
}

void loop() {
  ledcWrite(0, 128); // sound
  delay(1000);
  ledcWrite(0, 0);   // stop
  delay(1000);
}
