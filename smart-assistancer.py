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
    global scvalue
    text=event.widget.cget("text")
    print(text)
    speak(text)
    if text=="=":

        if scvalue.get().isdigit():
            value=int(scvalue.get())
            speak(str(value))
        else:
            try:
                value = eval(screen.get())
                speak(str(value))
            except Exception as e:
                print(e)
                scvalue.set("Syntax Error")
                speak("Syntax Error")
                screen.update()
        scvalue.set(value)
        screen.update()
    elif text=="Time":
        def time():
            string=strftime("%H:%M:%S %p")
            speak(string)
            scvalue.set(string)
            screen.update()
        time()
        
    elif text=="Date":
        def date():
            string=strftime('%d-%m-%Y')
            # string=strftime("%")
            speak(string)
            scvalue.set(string)
            screen.update()
        date()
    elif text=="Speak here !":

        def add():
            global temp
            temp=0
            for x in range(length):
                temp=temp+list[x]
            return(temp)

