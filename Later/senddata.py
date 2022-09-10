import serial
import time
import speech_recognition as sr
import pyaudio
r = sr.Recognizer()
arduino = serial.Serial(port="/dev/ttyACM0", baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    with sr.Microphone() as mic:
        print("Listening...")
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en_US helm')
        print("User said: ",query)
        if "hello" in query:
            a="1"
            write_read(a)
            time.sleep(2)
            a="0"
            write_read(a)
        else:
            a="0"
            write_read(a)
    except Exception:
        print("Say that again please...")

