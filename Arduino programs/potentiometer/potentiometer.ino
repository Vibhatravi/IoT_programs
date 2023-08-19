#include <Servo.h>

const int potentiometer = A0;
const int servoPin = 11;
Servo servo;

void setup() {
  servo.attach(servoPin);
  Serial.begin(9600);

}

void loop() {
  int potentiometervalue = analogRead(potentiometer);
  int angle = map(potentiometervalue,0,1023,0,180);
  servo.write(angle);
  Serial.print("Potentiometer: ");
  Serial.print(potentiometervalue);
  Serial.print(", Servo angle: ");
  Serial.println(angle);

  delay(15);
}
