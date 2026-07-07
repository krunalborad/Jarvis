import pywhatkit
import pyttsx3
import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


strTime = int(datetime.datetime.now().strftime("%H"))
update = int((datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    
    root = tk.Tk()
    root.withdraw()  

    
    speak("Who do you want to message?")
    choice = simpledialog.askstring("Select Person", "Enter 1 for Person 1 or 2 for Person 2:", parent=root)

    if choice == "1":
        speak("You chose Person 1")
        message = simpledialog.askstring("Message", "What is your message?", parent=root)
        if message:
            pywhatkit.sendwhatmsg("+918879905550", message, time_hour=strTime, time_min=update)
            speak("Message sent")
        else:
            speak("No message entered.")
    elif choice == "2":
        speak("You chose Person 2")
        message = simpledialog.askstring("Message", "What is your message?", parent=root)
        if message:
            pywhatkit.sendwhatmsg("+919833095550", message, time_hour=strTime, time_min=update)
            speak("Message sent")
        else:
            speak("No message entered.")
    else:
        speak("Invalid choice. Please enter 1 or 2.")


    root.destroy()

if __name__ == "__main__":
    sendMessage()