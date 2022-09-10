import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
            #It takes microphone input from the user and returns string output
            r = sr.Recognizer()
            with sr.Microphone() as mic:
                print("Listening...")
                speak("Listening...")
                r.adjust_for_ambient_noise(mic)
                audio = r.listen(mic)
            try:
                print("Recognizing...")
                speak("Recognizing...")
                query = r.recognize_google(audio, language='en_IN')
                print("you said",query)
                speak("you said")
                speak(query)
            except Exception:
                print("Say that again please...")
                speak("Say that again please...")
                return "None"
            return query
a=takeCommand()
print(a)
