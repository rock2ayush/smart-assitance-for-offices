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

        def mul():
           mu=1
           for x in range(len(list)):
                mu=mu*list[x]
           return(mu)
        def sub():
            global x
            global y
            x,y=list
            return(x-y)
        def division():
           x,y=list
           return(x/y)
        def reminder(): 
            x,y=list
            return(x%y)
        def SMALL():
            small=list[0]
            for x in range(1,length):
                if(small>list[x]):
                    small=list[x]
            return(small)
        def LARGE():
            large=list[0]
            for x in range(1,length):
                if(large<list[x]):
                    large=list[x]
            return(large)
        def HCF():
            for i in range(SMALL(),0,-1):
                for j in range(length):
                    if(length-1==j):
                        if(list[j]%i==0):
                            return(i)
                        else:
                            break


                    if(list[j]%i==0):
                        pass
                    else:
                        break
        def LCM():
            large=LARGE()
            for i in range(large,mul()+1,large):
                for j in range(length):
                    if(length-1==j):
                        if(i%list[j]==0):
                            return(i)
                    if(i%list[j]==0):
                        pass
                    else:
                        break

        def FIBONACCI():
                previous=0
                next=1
                temp=0
                for i in range(list[0]):
                    print(previous,end=' ')
                    fibo=str(previous)
                    speak(fibo)
                    scvalue.set(fibo)
                    temp=previous
                    previous=next
                    next=temp+previous
                screen.update()
                
        def FACTORIAL():
            fact=1
            for i in range(list[0],1,-1):
                fact=fact*i
            return(fact) 
        
        def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Good  morning")
                scvalue.set("Good  morning !")
                screen.update()
            elif hour>=12 and hour<18:
                speak("Good after noon")
                scvalue.set("Good afternoon !")
                screen.update()
            else:
                speak("Good evevning")
                scvalue.set("Good evevning !")
                screen.update()
        wishMe()
        print('Welcome to smart calculator')
        speak('Welcome to smart calculator')
        scvalue.set('Welcome Here!')
        screen.update()
        print('My name is SMART CALCI ')
        scvalue.set('My name is SMART CALCI ')
        screen.update()
        speak('My name is SMART CALCI ')

        i=1
        while(i):
            def takeCommand():

                #it take micro phone input from user as a input
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    scvalue.set("Listening...")
                    screen.update()
                    r.pause_threshold=1
                    audio=r.listen(source)
    
                try:
                    print("Recognizing...")
                    scvalue.set("Listening...")
                    screen.update()
                    query=r.recognize_google(audio,language='en-in')
                    print(query+" ")
                    # speak(query)
    
                except Exception as e:
                    
                    # print(e)
                    print("say that again please...")
                    return "None"
                return query
            if __name__ == '__main__':

                str1=takeCommand()  
            list=[]
            # str1=input("query")
            for s in str1.split():

                if(s.isdigit()):
                    list.append(eval(s))
            str2=str1.lower()
            length=len(list)

            if('close' in str2):
                   print("\nend the program ..")
                   scvalue.set("Thank you!")
                   screen.update()
                   speak("Thank you!, Welcome in smart calci")
                   
                   i=0

          
            elif('+' in str2 or 'sum' in str2 or 'plus' in str2 or 'add' in str2):
                    j=str(add())
                    print(j)
                    scvalue.set(j)
                    screen.update()
                    speak(j)
            elif('sub' in str2):
                    k=str(sub())
                    print(k)
                    scvalue.set(k)
                    screen.update()
                    speak(k)
            elif('mul' in str2):
                    l=str(mul())
                    print(l)
                    scvalue.set(l)
                    screen.update()
                    speak(l)
            elif('divi' in str2):
                  m=str(division())
                  print(m)
                  scvalue.set(m)
                  screen.update()
                  speak(m)
            elif('modu' in str2):
                 n=str(reminder())
                 print(n)
                 scvalue.set(n)
                 screen.update()
                 speak(n)

            elif('exp' in str2):
                 for x in str1.split():
                    if(x.isalpha()):
                        pass
                    else:
                       o=str(eval(x))
                       print(o)
                       scvalue.set(o)
                       screen.update()
                       speak(o)

            elif('hcf' in str2 or 'gcd' in str2):
                  p=str(HCF())
                  print(p)
                  scvalue.set(p)
                  screen.update()
                  speak(p)
            elif('lcm' in str2):
                q=str(LCM())
                print(q)
                scvalue.set(q)
                screen.update()
                speak(q)
            elif('fibon' in str2):
                # list[0]
                FIBONACCI()
                print('')
            elif('fact' in str2):
                 list[0]
                 f=str(FACTORIAL())
                 print(f)
                 scvalue.set(f)
                 screen.update()
                 speak(f)

            elif('boss' in str2):
                print('my boss name is Anand kumar verma')
                scvalue.set("Anand kumar verma")
                screen.update()
                speak('my boss name is Anand kumar verma')

            elif "open youtube" in str2:
                scvalue.set("You Tube ...")
                screen.update()
                webbrowser.open("youtube.com")
                break
                
            else:
                print("Please say again") 
                scvalue.set("Please say again")
                screen.update()
                speak("Please say again")


     # elif text=="Speak here !":
     #     screen.set("")
     #     screen.update()
     
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

scvalue= StringVar()
scvalue.set("")

screen=Entry(root, borderwidth=10,textvar=scvalue,font="lucide 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,bg="RED")
# b=Button(f,text="Speak here !",padx=29,pady=12,font="lucida 10 bold")
# b.pack(side=LEFT)
# b.bind("<Button-1>",click)
b=Button(f,text="Speak here !",padx=17,pady=10,font="lucida 10 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="Notepad",padx=30,pady=10,font="lucida 10 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="Date",padx=42,pady=10,font="lucida 10 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="Time",padx=36,pady=10,font="lucida 10 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()


f=Frame(root,bg="RED")
for i in range(7,10):
    
    b=Button(f,text=str(i),padx=28,pady=12,font="lucida 35 bold")
    b.pack(side=LEFT) 
    b.bind("<Button-1>",click)
b=Button(f,text="/",padx=29,pady=12,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="pink")
for i in range(4,7):  
    b=Button(f,text=str(i),padx=28,pady=12,font="lucida 35 bold")
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)
b=Button(f,text="%",padx=14,pady=12,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="green")

for i in range (1,4):
    b=Button(f,text=str(i),padx=28,pady=12,font="lucida 35 bold")
    b.pack(side=LEFT)
    b.bind("<Button-1>",click)
b=Button(f,text="+",padx=22,pady=12,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="0",padx=27,pady=12,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text=".",padx=34,pady=12,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=32,pady=12,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=24,pady=12,font="lucida 35 bold")
b.pack(side=LEFT)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="grey")
f.pack()


root.mainloop()
