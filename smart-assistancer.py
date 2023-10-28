from tkinter import *
import datetime

from time import strftime
import webbrowser
import pyttsx3
import speech_recognition as sr

root=Tk()
root.geometry("644x900")
# root.geometry("500x500")

root.title("Smart Calculator")


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

root.configure(background="cyan")
Button(text="Close",command=root.destroy).pack(fill=X)



def click(event):
