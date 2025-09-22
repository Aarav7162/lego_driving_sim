#include <NinjaIoT.h>

NinjaIoT iot;

const int irPin = D2;

void setup() {
  Serial.begin(115200);
  pinMode(irPin, INPUT);
  iot.connect("Atlantic", "24042006DD", "AK11");
}

void loop() {
  iot.ReadAll();

  int irValue = digitalRead(irPin);
  iot.WriteVar("braking_value", irValue);

  delay(1);
}
