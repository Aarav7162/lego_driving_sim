#include <NinjaIoT.h>
#include <Wire.h>

NinjaIoT iot;
int brakeValue = 0;

void setup() {
  Serial.begin(115200);
  iot.connect("wifi-name","wifi-pass","YOUR_UID");
}

void loop() {
  brakeValue = analogRead(A0);
  iot.WriteVar("braking_value", brakeValue);
  delay(100);
}
