int x;
const int ledPin=13;
const int leftLedPin=11;
const int rightLedPin=12;
const int rightSensorPin=7;
const int leftSensorPin=8;
boolean rightVal = 0;
boolean leftVal = 0;

void setup()
{
  pinMode(leftLedPin, OUTPUT);
  pinMode(rightLedPin, OUTPUT);
  pinMode(leftSensorPin, INPUT);
  pinMode(rightSensorPin, INPUT);
  Serial.begin(115200);
 Serial.setTimeout(1);
   pinMode(ledPin,OUTPUT);  
}
 
void loop ()
{
  //x=1;
  while (!Serial.available());
 x = Serial.readString().toInt();
  rightVal =digitalRead(rightSensorPin);
  leftVal =digitalRead(leftSensorPin);
  if(x == 1){
    digitalWrite(ledPin, HIGH);
    delay(1000);
  if (leftVal==LOW && rightVal==LOW)
  {
    // if no sound detected, no LED will light up
    digitalWrite(leftLedPin, LOW);
    digitalWrite(rightLedPin, LOW);
    Serial.println("None");
  }
  else if (leftVal==LOW && rightVal==HIGH)
  {
    // if sound detected on the right, the right LED will light up
    digitalWrite(leftLedPin, LOW);
    digitalWrite(rightLedPin, HIGH);
    delay(100);
        digitalWrite(rightLedPin, HIGH);
        delay(100);
    Serial.println("Right");
  }
  else if (leftVal==HIGH && rightVal==LOW)
  {
    // if sound detected on the left, the left LED will light up
    digitalWrite(leftLedPin, HIGH);
        delay(100);
        digitalWrite(rightLedPin, HIGH);
        delay(100);
    digitalWrite(rightLedPin, LOW);
    Serial.println("Left");
  }
  else
  {
    // else both LEDs will light up indicating that both sensors detected sound
    digitalWrite(leftLedPin, HIGH);
        delay(100);
        digitalWrite(rightLedPin, HIGH);
        delay(100);
    digitalWrite(rightLedPin, HIGH);
        delay(100);
        digitalWrite(rightLedPin, HIGH);
        delay(100);
    Serial.println("Both");
  }
 }
 
 }
