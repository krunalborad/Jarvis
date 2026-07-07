# Jarvis Pro Version - Full Desktop Assistant
# Features: Wake Word, Animated GUI, Natural TTS, Full Commands, Stable Execution
 
import datetime
import os
import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox
from SearchNow import searchGoogle, searchYoutube, searchWikipedia
from ai_handler import ask_rapidapi
from PIL import Image, ImageTk
 
# --------------------------- Text-to-Speech ---------------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
 
is_muted = False
 
def speak(audio):
    def _speak():
        eng = pyttsx3.init("sapi5")
        eng.setProperty("rate", 170)
        eng.say(audio)
        eng.runAndWait()
    t = threading.Thread(target=_speak)
    t.start()
    t.join()
 
# --------------------------- Wake Word Detection ---------------------------
def listen_wake_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Waiting for wake word 'Hey Jarvis'...")
        while True:
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                command = r.recognize_google(audio, language='en-in').lower()
                if "hey jarvis" in command:
                    speak("Yes sir, I am awake")
                    return
            except sr.WaitTimeoutError:
                continue
            except:
                continue
 
# --------------------------- Command Input ---------------------------
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return None
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}")
    except:
        print("Say that again...")
        return None
    return query
 
# --------------------------- Mute Toggle ---------------------------
def toggle_mute():
    global is_muted
    pyautogui.press("m")
    if is_muted:
        speak("Video unmuted")
    else:
        speak("Video muted")
    is_muted = not is_muted
 
# --------------------------- Confirmation Dialog ---------------------------
def confirm_action(action):
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askquestion("Confirm Action", f"Do you wish to {action} your computer?", parent=root)
    root.destroy()
    return response == 'yes'
 
# --------------------------- Execute Commands ---------------------------
def executeCommand(query):
    global is_muted
    if not query:
        return
    query = query.lower()
    query = query.replace("jarvis", "").strip()
 
    # --- Wake / Sleep ---
    if "wake up" in query:
        from GreetMe import greetMe
        greetMe()
        speak("Hello sir, I am awake now. Waiting for your commands.")
        return
    if "go to sleep" in query:
        speak("Ok sir, you can call me anytime")
        return
 
    # --- AI Query ---
    elif 'using ai' in query:
        query = query.replace("using ai", "")
        query = query.replace("using AI", "")
        query = query.replace("using aI", "")
        query = query.replace("using Ai", "")
        print("Processing via AI...")
        speak("Processing your request via AI...")
        answer = ask_rapidapi(query)
        print(f"Answer: {answer}")
        speak("Here is your answer.")
        return
 
    # --- Screenshots / Camera ---
    elif "show screenshot" in query:
        screenshot_path = "ss.jpg"
        if os.path.exists(screenshot_path):
            os.startfile(screenshot_path)
            speak("Here is the screenshot")
            pyautogui.sleep(3)
            pyautogui.hotkey("alt", "f4")
        else:
            speak("Screenshot not found")
        return
    elif "screenshot" in query:
        im = pyautogui.screenshot()
        im.save("ss.jpg")
        pyautogui.sleep(2)
        speak("Screenshot taken")
        return
    elif "click my photo" in query:
        pyautogui.press("super")
        pyautogui.typewrite("camera", 0.1)
        pyautogui.press("enter")
        pyautogui.sleep(2)
        speak("SMILE")
        pyautogui.press("enter")
        pyautogui.sleep(2)
        pyautogui.hotkey("alt", "f4")
        pyautogui.sleep(2)
        speak("Photo Taken")
        return
 
    # --- Conversations ---
    elif "hello" in query:
        speak("Hello sir, how are you?")
        return
    elif "i am fine" in query:
        speak("That's great, sir")
        return
    elif "how are you" in query:
        speak("Perfect, sir")
        return
    elif "thank you" in query:
        speak("You're welcome, sir")
        return
 
    # --- Media Controls ---
    elif "pause" in query or "play" in query:
        pyautogui.press("k")
        speak("Video toggled")
        return
    elif "mute" in query or "unmute" in query:
        toggle_mute()
        return
    elif "volume up" in query:
        from keyboard import volumeup
        speak("Turning volume up")
        volumeup()
        return
    elif "volume down" in query:
        from keyboard import volumedown
        speak("Turning volume down")
        volumedown()
        return
 
    # --- Browser Commands ---
    elif "open chrome" in query:
        chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
        if os.path.exists(chrome_path):
            os.startfile(chrome_path)
            speak("Google Chrome is open, sir")
        else:
            speak("Chrome not found, check installation path")
        return
    elif "maximize the window" in query:
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('x')
        speak("Window maximized")
        return
    elif "new window" in query:
        pyautogui.hotkey('ctrl', 'n')
        speak("New window opened")
        return
    elif "incognito window" in query:
        pyautogui.hotkey('ctrl', 'shift', 'n')
        speak("Incognito window opened")
        return
    elif "minimise the window" in query:
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('n')
        speak("Window minimized")
        return
    elif "history" in query:
        pyautogui.hotkey('ctrl', 'h')
        speak("History opened")
        return
    elif "downloads" in query:
        pyautogui.hotkey('ctrl', 'j')
        speak("Downloads opened")
        return
    elif "previous tab" in query:
        pyautogui.hotkey('ctrl', 'shift', 'tab')
        speak("Previous tab")
        return
    elif "next tab" in query:
        pyautogui.hotkey('ctrl', 'tab')
        speak("Next tab")
        return
    elif "close window" in query:
        pyautogui.hotkey('ctrl', 'shift', 'w')
        speak("Window closed")
        return
    elif "close chrome" in query:
        os.system("taskkill /f /im chrome.exe")
        speak("Chrome closed")
        return
 
    # --- Paint Drawing ---
    elif "draw a line" in query:
        pyautogui.moveTo(267, 387, duration=1)
        pyautogui.click()
        pyautogui.dragRel(267, 0, 1)
        speak("Line drawn")
        return
    elif "draw a square" in query:
        pyautogui.moveTo(1308, 376, duration=1)
        pyautogui.click()
        distance = 300
        for i in range(1):
            pyautogui.dragRel(distance, 0, duration=0.5)
            pyautogui.dragRel(0, distance, duration=0.5)
            pyautogui.dragRel(-distance, 0, duration=0.5)
            pyautogui.dragRel(0, -distance, duration=0.5)
        speak("Square drawn")
        return
    elif "draw a rectangular spiral" in query:
        pyautogui.moveTo(300, 393, duration=1)
        pyautogui.click()
        distance = 300
        while distance > 0:
            pyautogui.dragRel(distance, 0, 0.1, button="left")
            distance -= 10
            pyautogui.dragRel(0, distance, 0.1, button="left")
            pyautogui.dragRel(-distance, 0, 0.1, button="left")
            distance -= 10
            pyautogui.dragRel(0, -distance, 0.1, button="left")
        speak("Rectangular spiral drawn")
        return
    elif "erase it" in query:
        pyautogui.hotkey('ctrl', 'z')
        speak("Erased")
        return
 
    # --- System Commands ---
    elif "shutdown the system" in query:
        speak("Are you sure you want to shutdown?")
        if confirm_action("shutdown"):
            os.system("shutdown /s /t 1")
        else:
            speak("Shutdown canceled")
        return
    elif "restart the system" in query:
        speak("Are you sure you want to restart?")
        if confirm_action("restart"):
            os.system("shutdown /r /t 5")
        else:
            speak("Restart canceled")
        return
    elif "finally sleep" in query:
        speak("Going to sleep, sir")
        exit()
 
    # --- Search ---
    elif "google" in query:
        searchGoogle(query)
        return
    elif "youtube" in query:
        searchYoutube(query)
        return
    elif "wikipedia" in query:
        searchWikipedia(query)
        return
 
    elif "news" in query:
        from NewsRead import latestnews
        latestnews()
        return
 
    elif "calculate" in query:
        from Calculatenumbers import Calc
        query = query.replace("calculate","").replace("echo","")
        Calc(query)
        return
 
    elif "whatsapp" in query:
        from Whatsapp import sendMessage
        sendMessage()
        return
 
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir, the time is {strTime}")
        return
 
    elif "refresh" in query:
        pyautogui.hotkey('win', 'd')
        time.sleep(1)
        pyautogui.press('f5')
        speak("PC refreshed")
        return
 
    elif "scroll down" in query:
        speak("Scrolling down")
        for _ in range(5):
            pyautogui.scroll(100)
            time.sleep(0.5)
        speak("Scrolled down")
        return
    elif "scroll up" in query:
        speak("Scrolling up")
        for _ in range(5):
            pyautogui.scroll(-100)
            time.sleep(0.5)
        speak("Scrolled up")
        return
 
    elif "type" in query:
        query = query.replace("type", "")
        pyautogui.write(f"{query}", interval=0.1)
        pyautogui.press("enter")
        speak("Typed")
        return
 
# --------------------------- GUI ---------------------------
def animated_gui():
    root = tk.Tk()
    root.title("Jarvis AI Pro")
    root.geometry("400x400")
    root.configure(bg="black")
    canvas = tk.Canvas(root, width=400, height=400, bg="black", highlightthickness=0)
    canvas.pack()
    frames = [ImageTk.PhotoImage(Image.open(f'../frames2/frame_{i:04d}.jpg').resize((400, 400))) for i in range(89)]
    img_id = canvas.create_image(200, 200, image=frames[0])
    def update(ind):
        canvas.itemconfig(img_id, image=frames[ind])
        root.after(50, update, (ind+1) % 89)
    update(0)
    root.mainloop()
 
# --------------------------- Main ---------------------------
if __name__ == "__main__":
    gui_thread = threading.Thread(target=animated_gui)
    gui_thread.daemon = True
    gui_thread.start()
 
    while True:
        listen_wake_word()
        while True:
            query = takeCommand()
            if query is None:
                break
            executeCommand(query)