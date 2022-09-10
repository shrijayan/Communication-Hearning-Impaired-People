	
import serial 
import time
arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
while True:
    try:
        data = arduino.readline()
        if data:
            print(data)
            print('Hi Arduino')
    except:
        arduino.close() 
