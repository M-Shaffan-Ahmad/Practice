import pyttsx3
from tkinter import *
import databse

engine = pyttsx3.init()

def save(filename,text):
    engine.save_to_file(text, '{}.mp3'.format(filename))
    play()



def volume_d():
    engine.setProperty("volume", engine.getProperty("volume")-0.1)
    play()
def volume_u():
    engine.setProperty("volume", engine.getProperty("volume")+0.1)
    play()
def rate_d():
    engine.setProperty("rate", engine.getProperty("rate")-50)
    print(engine.getProperty("rate"))
    play()
def rate_u():
    engine.setProperty("rate", engine.getProperty("rate")+50)
    print(engine.getProperty("rate"))
    play()

def rate(rate=200):
    engine.setProperty('rate', rate)

def voice_m():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    play()

def voice_f():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    play()

def play():
    engine.runAndWait()

def dis(name,text="Please enter something"):
    databse.database_up(text, name+".mp3")
    engine.say(text)
    play()







