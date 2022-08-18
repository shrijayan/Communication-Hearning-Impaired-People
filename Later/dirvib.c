const int ledPin=13;
String nom = "Arduino";
String msg;
void setup() {
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
}

void loop() {
  readSerialPort();

  if (msg == "data") {
    //sendData();
  }else if(msg=="led0"){
    digitalWrite(ledPin,LOW);
    Serial.println(" Arduino set led to LOW");
  }else if(msg=="led1")
  {
    digitalWrite(ledPin,HIGH);
   Serial.println(" Arduino set led to HIGH");
   delay(5000);
   }
   else if(msg!="led0" || msg!="led1"){
  digitalWrite(ledPin,LOW);
  }

}

void readSerialPort() {
  msg = "";
  if (Serial.available()) {
    delay(10);
    while (Serial.available() > 0) {
      msg += (char)Serial.read();
     
    }
    Serial.flush();
  }
}
/*void sendData() {
  //write data ledState x sensor1 x sensor2
  Serial.print(digitalRead(ledPin));
  Serial.print("x");
  Serial.print(analogRead(A0));
  Serial.print("x");
  Serial.print(analogRead(A1));
}*/
