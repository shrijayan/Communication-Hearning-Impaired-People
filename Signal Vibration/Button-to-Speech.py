import RPi.GPIO as GPIO
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices') 
for voice in voices:
    engine.setProperty('voice', 'english_rp+f5')

def speak(text):
    engine.say(text)
    engine.runAndWait() 
def one():
	GPIO.setwarnings(False)
	GPIO .setmode(GPIO.BOARD)
	inPin = 31
	inPin1= 12


	GPIO.setup(inPin,GPIO.IN)
	GPIO.setup(inPin1,GPIO.IN)


	a = GPIO.input(inPin)
	b = GPIO.input(inPin1)


	if(a==1):
            text="plese help me"
            print(text)
            speak(text)
	elif(b==1):
            text="Can you repeat again?"
            print(text)
            speak(text)

a=1
while a==1:
    one()
