import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {
    "command prompt": "cmd",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "chrome": "chrome",
    "notepad": "notepad",
    "vs code": "code",
    "powerpoint": "powerpnt"
}

def openappweb(query):
    speak("Launching, sir")
    if any(ext in query for ext in [".com", ".co.in", ".org"]):
        query = query.replace("open", "").replace("echo", "").replace("launch", "").replace(" ", "")
        try:
            webbrowser.open(f"https://www.{query}")
        except Exception as e:
            speak("Sorry, I couldn't open the website.")
            print(f"Error opening website: {e}")
    else:
        query = query.lower()
        for app, cmd in dictapp.items():
            if app in query:
                try:
                    os.system(f"start {cmd}")
                    break 
                except Exception as e:
                    speak(f"Sorry, I couldn't open {app}.")
                    print(f"Error opening app: {e}")

def closeappweb(query):
    speak("Closing, sir")
    tab_count = None
    try:
        if "one tab" in query or "1 tab" in query:
            tab_count = 1
        elif "two tab" in query or "2 tab" in query:
            tab_count = 2
        elif "three tab" in query or "3 tab" in query:
            tab_count = 3
        elif "four tab" in query or "4 tab" in query:
            tab_count = 4
        elif "five tab" in query or "5 tab" in query:
            tab_count = 5
        if tab_count:
            for _ in range(tab_count):
                pyautogui.hotkey("ctrl", "w")
                sleep(0.5)
            speak(f"{tab_count} tabs closed")
        else:
            for app, cmd in dictapp.items():
                if app in query:
                    os.system(f"taskkill /f /im {cmd}.exe")
    except Exception as e:
        speak("Sorry, I couldn't close the tabs.")
        print(f"Error closing tabs: {e}")