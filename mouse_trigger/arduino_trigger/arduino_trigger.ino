// Waits for the character 'T' over USB serial.
// When it arrives, pulses TRIGGER_PIN HIGH for PULSE_MS and replies "OK".

const int TRIGGER_PIN = 13;     // 13 = onboard LED, handy for testing
const unsigned long PULSE_MS = 10;

void setup() {
  pinMode(TRIGGER_PIN, OUTPUT);
  digitalWrite(TRIGGER_PIN, LOW);
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == 'T') {
      digitalWrite(TRIGGER_PIN, HIGH);
      delay(PULSE_MS);
      digitalWrite(TRIGGER_PIN, LOW);
      Serial.println("OK");
    }
  }
}
