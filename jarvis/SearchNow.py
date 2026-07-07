import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    query = query.replace("echo", "").replace("google search", "").replace("google", "")
    speak("Searching Google...")
    
    try:
        pywhatkit.search(query)  
        speak("Here are the results for your query.")
    except Exception as e:
        speak("I couldn't search on Google, please try again.")

def searchYoutube(query):
    query = query.replace("echo", "").replace("youtube search", "").replace("youtube", "")
    speak("Searching on YouTube...")
    
    try:
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Here are the results.")
    except Exception as e:
        speak("I couldn't search YouTube, please try again.")

def searchWikipedia(query):
    query = query.replace("echo", "").replace("wikipedia", "").replace("search wikipedia", "")
    speak("Searching Wikipedia...")
    
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia...")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results, please be more specific.")
    except Exception as e:
        speak("I couldn't retrieve the Wikipedia information, please try again.")