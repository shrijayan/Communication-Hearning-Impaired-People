import serial,time
import speech_recognition as sr

a="led1"
def hear():
	ear=sr.Recognizer()
	with sr.Microphone() as source:
		print("listening....")
		audio = ear.listen(source , phrase_time_limit=2)
		try:
			text = ear.Recognize_google(audio)
			print(text)
			if "hello" in text :
				a="led1"
				print(a)

			else:
				a="led0"
				print("else")
		except:
			a = "led0"
			hear()
			
		serial.Serial("dev/ttyACM0",9600).close()
hear()

if__name__=='__main__':
	serial.Serial("dev/ttyACM0",9600)

	print('Running...press crtl c to exit..')
	with serial.Serial("dev/ttyACM0",9600,timeout=1) as arduino:
		time.sleep(0.9)
	if arduino.isOpen():
		print("{} Connected!".format(arduino.port))
	try:
		msg=a
		print(arduino.write(msg.encode()))
	except:
		pass
