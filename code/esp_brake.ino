#include <NinjaIoT.h>

NinjaIoT iot;

const int irPin = D2;

void setup() {
  Serial.begin(115200);
  pinMode(irPin, INPUT);
  iot.connect("WiFi_Name", "WiFi_Pass", "Platform_UID");
}

void loop() {
  iot.ReadAll();

  int irValue = digitalRead(irPin);
  iot.WriteVar("braking_value", irValue);

  delay(1);
}
