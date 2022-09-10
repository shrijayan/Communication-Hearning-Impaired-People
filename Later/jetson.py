import serial
import time
import speech_recognition as sr
a="led1"
if __name__ == '__main__':
    #serial.Serial("/dev/ttyACM0", 9600)
   
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            
            print("{} connected!".format(arduino.port))
            cmd= a
            arduino.write(cmd.encode())		

