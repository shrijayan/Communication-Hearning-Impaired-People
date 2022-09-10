
import serial
with serial.Serial('/dev/ttyACM0', 9600, timeout=10) as ser:  # open serial port
    while True:
        print(ser.readline())
