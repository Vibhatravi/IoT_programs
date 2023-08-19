
void setup() {
  Serial.begin(9600);
  

}

void loop() {
  // put your main code here, to run repeatedly:
 int s1= analogRead(A0);
 Serial.println(s1);
 delay(5000); 
}
