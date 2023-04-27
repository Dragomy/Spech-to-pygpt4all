import speech_recognition as sr
from pygpt4all.models.gpt4all_j import GPT4All_J

import os
from gtts import gTTS

r = sr.Recognizer()
def new_text_callback(text):
    print(text, end="")

with sr.Microphone() as source:
    print("Say something!")
    audio_data = r.record(source, duration=15)
    print("STOP,its waitin time")

text = r.recognize_google(audio_data)
    
model = GPT4All_J('PATH TO: ggml-gpt4all-j-v1.3-groovy.bin') #YOU NEED TO EDIT THIS
model.generate(text, n_predict=42, new_text_callback=new_text_callback)        #Change n_predict to change number of output tokens 
