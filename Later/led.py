import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
inputPin=15
outputPin=23
lightState=False
buttonStateOld=True
GPIO.setup(inputPin,GPIO.IN)
GPIO.setup(outputPin,GPIO.OUT)
while(1==1):
    buttonStateNew=GPIO.input(inputPin)
    if buttonStateOld==True and buttonStateNew==False:
        lightState=not(lightState)
    GPIO.output(outputPin,lightState)
    x=GPIO.input(inputPin)
    print(x)
    buttonStateOld=buttonStateNew

	    
	

