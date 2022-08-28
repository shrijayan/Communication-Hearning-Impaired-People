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
  Serial.begin (9600);
}
 
void loop ()
{
  // check microphone sensors for sound
  rightVal =digitalRead(rightSensorPin);
  leftVal =digitalRead(leftSensorPin);
 
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
    delay(200);
    Serial.println("Right");
  }
  else if (leftVal==HIGH && rightVal==LOW)
  {
    // if sound detected on the left, the left LED will light up
    digitalWrite(leftLedPin, HIGH);
        delay(200);

    digitalWrite(rightLedPin, LOW);
    Serial.println("Left");
  }
  else
  {
    // else both LEDs will light up indicating that both sensors detected sound
    digitalWrite(leftLedPin, HIGH);
    digitalWrite(rightLedPin, HIGH);
    
    Serial.println("Both");
  }
}
