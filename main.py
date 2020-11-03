import os
import time
import speech_recognition as sr
import playsound
from gtts import gTTS

def speech(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        audio = rec.listen(source)
        speech_text = ""

        try:
            speech_text = rec.recognize_google(audio)
            print(speech_text)
        except Exception as e:
            print("Exception "+ str(e))
    
    return speech_text

print("Please enter the text: \n")

text = input()
speech(text)
get_audio()
