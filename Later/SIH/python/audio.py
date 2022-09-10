import speech_recognition as sr
import pyaudio
import serial
import time
from twilio.rest import Client 
r = sr.Recognizer()
arduino = serial.Serial(port="/dev/ttyACM0", baudrate=115200, timeout=.1)
def msg():
	account_sid = 'AC7879cd351441a3e37b56f517d052de2b' 
	auth_token = 'ea18149bdae6f9dd106293078647cba1'  
	client = Client(account_sid, auth_token) 
 
	message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Someone called you',      
                              to='whatsapp:+916379440984'  
                          ) 
 
	print("SMS Send")
def hello():
	def write_read(x):
    	    arduino.write(bytes(x, 'utf-8'))
    	    time.sleep(0.05)
    	    data = arduino.readline()
    	    return data
	with sr.Microphone() as mic:
    	    print("Listening...")
    	    r.adjust_for_ambient_noise(mic)
    	    audio = r.listen(mic)
	try:
	    print("Recognizing...")
	    query = r.recognize_google(audio, language='en_IN')
	    query=query.lower()
	    print("User said: ",query)
	    if "hello" in query:
	        a="1"
	        write_read(a)
	        msg()
	        exit(0)
	    else:
	        hello()
	        a="0"
	        write_read(a)
	        hello()
	except Exception:
    	    print("Say that again please...")


hello()

	
