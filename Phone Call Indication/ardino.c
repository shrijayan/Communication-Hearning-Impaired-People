int LED1=8;  // red to change

int tx=1;
int rx=0;
char inSerial[15];


void setup(){
  Serial.begin(9600);  
  pinMode(LED1, OUTPUT);
  
  pinMode(tx, OUTPUT);
  pinMode(rx, INPUT);
  delay(2000);
  digitalWrite(LED1, HIGH);  // blink 3x to show it's on
  delay(500);
  digitalWrite(LED1, LOW);
  delay(500);
  digitalWrite(LED1, HIGH);
  delay(500);
  digitalWrite(LED1, LOW);
  delay(500);
  digitalWrite(LED1, HIGH);
  delay(500);
  digitalWrite(LED1, LOW);
}

void loop(){
  int i=0;
  delay(500);
  if (Serial.available() > 0) {
  while (Serial.available() > 0) {
  inSerial[i]=Serial.read();
  i++;
  }
  inSerial[i]='\0';
  Check_Protocol(inSerial);
  }
}

void Check_Protocol(char inStr[]){
  int i=0;
  int m=0;
  Serial.println(inStr);
  if (!strcmp(inStr,"Off")){    //Led1 Off  
    digitalWrite(LED1, LOW);
    Serial.println("Off");  // only used for debugging
    for(m=0;m<11;m++){      // clears out buffered data so it doesn't keep seeing it and repeat
      inStr[m]=0;}
    }
  if (!strcmp(inStr,"On")){     //Led 1 on
    digitalWrite(LED1, HIGH);
    Serial.println("On"); // only used for debugging
    for(m=0;m<11;m++){    // clears out buffered data so it doesn't keep seeing it and repeat
      inStr[m]=0;}
    }
  else{
    for(m=0;m<11;m++){  // clears out buffered data so it doesn't keep seeing it and repeat
      inStr[m]=0;}
  i=0;
  }
}
