/*
 File/Sketch Name: SoundDirectionTester

 Version No.: v1.0 Created 14 August, 2019
 
 Original Author: Clyde A. Lettsome, PhD, PE, MEM
 
 Description:  This code/sketch makes finding the general direction of sound easy. This code/sketch drives two LEDs to indicate which of two microphones is receiving an audible sound.
 If both microphone sensors detect sound, both (left and right) LEDs light indicating that both microphones have detected sound. If one microphone sensor (left or right) detects sound,
 then the corresponding LED (left or right) will light up. If no microphone sensor detect sound, then no LED will light up.

 License: This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License (GPL) version 3, or any later
 version of your choice, as published by the Free Software Foundation.

 Notes: Copyright (c) 2019 by C. A. Lettsome Services, LLC
 For more information visit https://clydelettsome.com/blog/2019/08/15/my-weekend-project-sound-direction-tester/

 */

const int leftLedPin=13;
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
    Serial.println("Right");
  }
  else if (leftVal==HIGH && rightVal==LOW)
  {
    // if sound detected on the left, the left LED will light up
    digitalWrite(leftLedPin, HIGH);
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
