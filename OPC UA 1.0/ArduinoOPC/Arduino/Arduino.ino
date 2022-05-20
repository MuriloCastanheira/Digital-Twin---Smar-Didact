#include <AFMotor.h>
int x,por;

AF_DCMotor motor(3);

void setup() {
  motor.setSpeed(0);
  Serial.begin(9600);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString().toInt(); 
  motor.setSpeed((255*x)/100);
  motor.run(FORWARD);
  delay(100);
  Serial.print((255*x)/100);
}
