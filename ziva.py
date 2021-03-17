from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices[1].id) 
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good aftrnoon")
    else:
        speak("good evening")
    speak("saswat i am your assistant !! please tell me how may i help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.operation_timeout = 3
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print("say that again please.....")
        return "none"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stock' in query:
            webbrowser.open("stackoverflow.com")          
        elif 'play music' in query:
            music_dir = 'F:\\music'
            music =os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir, music[10]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"sir the time is (strtime)")
        elif 'open code' in query:
            codePath = "C:\\Users\\saswa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"        
            os.startfile(codePath)
        elif 'my college' in query:
            webbrowser.open('vssut.ac.in') 
        elif 'instagram' in query:
            webbrowser.open('instagram.com')           