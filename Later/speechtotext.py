
# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import speech_recognition as sr
# Sampling frequency
freq = 44100
  
# Recording duration
duration = 5
  
# Start recorder with the given values 
# of duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
  
# Record audio for the given number of seconds
sd.wait()
  
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)
  
# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)

def SpeechToText():
    r = sr.Recognizer()   #Speech recognition
    audio = sr.AudioFile("recording1.wav")
    with audio as source:
        print("Wait. Program Starting")
        audio = r.record(source)
        message = r.recognize_google(audio)
        print("Check: "+message)
    return message
print(SpeechToText())
