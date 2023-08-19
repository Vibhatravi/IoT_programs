int trigPin = 5;
int echoPin = 6;

int redLed = 11;
int blueLed = 10;
int greenLed = 9;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  long duration = pulseIn(echoPin,HIGH);
  long inches = microsecondsToInches(duration);
  long cms = microsecondsToCentimeters(duration);
  Serial.print("Distance: ");
  Serial.print(inches);
  Serial.print("in, ");
  Serial.print(cms);
  Serial.println("cm");
  delay(1000);
  long distance = duration*0.034/2;
//  Serial.print("Distance: ");
//  Serial.println(distance);
//  delay(5000);
  if (cms<10)
  {
    digitalWrite(redLed,HIGH);
    delay(5000);
    digitalWrite(redLed,LOW);
    delay(1000);
  }
  else if (cms>=10 && cms<=25)
  {
    digitalWrite(blueLed,HIGH);
    delay(5000);
    digitalWrite(blueLed,LOW);
    delay(1000);
  }
  else
  {
    digitalWrite(greenLed,HIGH);
    delay(5000);
    digitalWrite(greenLed,LOW);
    delay(1000);
  }
}

long microsecondsToInches(long microseconds) {
  return microseconds /74 /2;
}

long microsecondsToCentimeters(long microseconds) {
  return microseconds /29 /2;
}
