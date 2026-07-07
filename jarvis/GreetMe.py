import pyttsx3
import datetime


engine = pyttsx3.init("sapi5")
engine.setProperty("voice", engine.getProperty("voices")[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    """Function to greet based on the time of the day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, sir.")
    elif 12 <= hour < 18:
        speak("Good Afternoon, sir.")
    else:
        speak("Good Evening, sir.")

    speak("Please tell me, how can I help you?")