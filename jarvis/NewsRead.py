import requests
import pyttsx3
import tkinter as tk
from tkinter import simpledialog, messagebox


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=24e5ff6fdb83424980ea58bb4d626b9d",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=24e5ff6fdb83424980ea58bb4d626b9d",
        "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=24e5ff6fdb83424980ea58bb4d626b9dd",
        "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=24e5ff6fdb83424980ea58bb4d626b9d",
        "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=24e5ff6fdb83424980ea58bb4d626b9d",
        "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=24e5ff6fdb83424980ea58bb4d626b9d"
    }

    
    root = tk.Tk()
    root.withdraw()  


    speak("Which field news do you want?")
    field = simpledialog.askstring("News Category", "Which field news do you want? [business, health, technology, sports, entertainment, science]", parent=root)

    if not field:
        speak("No input provided.")
        root.destroy()
        return

    url = api_dict.get(field.lower(), None)
    if not url:
        speak("Sorry, I didn't understand the category. Please try again.")
        root.destroy()
        return

    try:
        news_response = requests.get(url)
        news_response.raise_for_status()  
        news = news_response.json()

        speak("Here is the first news.")
        articles = news.get("articles", [])

        if not articles:
            speak("No news articles found.")
            root.destroy()
            return

        for article in articles:
            title = article.get("title", "No title available")
            url = article.get("url", "")
            speak(title)
            print(title)
            print(f"For more info, visit: {url}")

            while True:
                a = simpledialog.askstring("Continue", "[Type 1 to continue or 2 to stop]: ", parent=root)
                if a == "1":
                    break
                elif a == "2":
                    speak("Stopping news updates.")
                    root.destroy()
                    return
                else:
                    speak("Invalid input. Please type 1 to continue or 2 to stop.")

        speak("That's all the news for now.")

    except requests.RequestException as e:
        speak("Sorry, there was an error fetching the news.")
        print(f"Error: {e}")

    
    root.destroy()

if __name__ == "__main__":
    latestnews()