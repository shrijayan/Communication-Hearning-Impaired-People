#import library
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
r = sr.Recognizer()

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 
output = sr.AudioFile('output.wav')
with output as source:
	audio = r.record(source)
print(r.recognize_google(audio))
