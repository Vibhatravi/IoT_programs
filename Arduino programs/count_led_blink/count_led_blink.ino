void setup(){
  pinMode(LED_BUILTIN,OUTPUT);
  Serial.begin(9600);
}
void loop(){
    int ledBlink=0;
  while(Serial.available()){
    Serial.println("Enter number");
    int input=Serial.parseInt();
//    Serial.println(input);
    for(int i=0;i<=input;i++){
      digitalWrite(LED_BUILTIN,HIGH);
      delay(200);
      ledBlink=ledBlink+1;
      Serial.println("Led Blinked");
      digitalWrite(LED_BUILTIN,LOW);
      delay(200);
    }
    Serial.print("NO of times led blinked: ");
    Serial.println(ledBlink);
  }
}
