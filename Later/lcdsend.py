# Importing Libraries
import serial
import time
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import speech_recognition as sr
from time import sleep
arduino = serial.Serial(port='/dev/ttyACM1', baudrate=115200, timeout=.1)
freq = 44100
  
# Recording duration
duration = 5
a=1
  
# Start recorder with the given values 
# of duration and sample frequency
def all():
	recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
  
# Record audio for the given number of seconds
	sd.wait()
  
# This will convert the NumPy array to an audio
# file with the given sampling frequency
	write("recording0.wav", freq, recording)
  
# Convert the NumPy array to audio file
	wv.write("recording1.wav", recording, freq, sampwidth=2)

	def SpeechToText():
            r = sr.Recognizer()   #Speech recognition
            audio = sr.AudioFile("recording1.wav")
            with audio as source:
                print("Wait. Recognizing..")
                audio = r.record(source)
                message = r.recognize_google(audio)
                #print("Check: "+message)
            return message

	def write_read(x):
            arduino.write(bytes(x, 'utf-8'))

# num = input("Enter a string: ") # Taking input from user
	text=SpeechToText()
	print(text)
	value = write_read(text)
while a==1:
	print("Speak.............")
	all()
	
