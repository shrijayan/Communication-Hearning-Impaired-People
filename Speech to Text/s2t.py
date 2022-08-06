import speech_recognition as sr
import time  
def hear():
    ear = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = ear.listen(source, phrase_time_limit=2)
        try:
            text = ear.recognize_google(audio)
            print(text)
            if "hello" in text:
                print("if")
                hear()
            else:
                hear()
                print("else")
        except:
            print("except")
            hear()
hear()
