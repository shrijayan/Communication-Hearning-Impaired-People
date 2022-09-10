while(True):
	def ok():
		import RPi.GPIO as GPIO
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(15,GPIO.IN)
		x=GPIO.input(15)
		print(x)

'''
		if(x==1):
			
			import cv2
			from PIL import Image
			import os
			import pyttsx3
			engine=pyttsx3.init()
			engine.setProperty('rate', 130)
			videoCaptureObject = cv2.VideoCapture(0)
			result = True
			while(result):
		    		ret,frame = videoCaptureObject.read()
		    		cv2.imwrite("NewPicture.jpg",frame)
			videoCaptureObject.release()
			cv2.destroyAllWindows()

			os.system('python3 detectnet.py NewPicture.jpg Output.jpg')

			infile = "read.text"
			f = open(infile, 'r')
			theText = f.read()
			f.close()
			engine.say(theText)
			engine.runAndWait()
			x=GPIO.input(15)
		else:
			ok()'''
ok()


