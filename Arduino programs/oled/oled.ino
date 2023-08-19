#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 32

//Adafruit_SSD1306 display(SCREEN_WIDTH,SCREEN_HEIGHT,&Wire,-1);
#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);

int trigPin = 5;
int echoPin = 6;

int redLed = 11;
int blueLed = 10;
int greenLed = 9;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

//  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
//    Serial.println(F("SSD1306 allocation failed"));
//    for(;;);
//  }
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);

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
  
  //delay(2000);
  display.clearDisplay();

  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,1);

  display.println("Distance: ");
  display.print(inches);
  display.print("in,");
  display.print(cms);
  display.println("cm");
  display.display();

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
