import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.IN)
x = GPIO.input(15)


