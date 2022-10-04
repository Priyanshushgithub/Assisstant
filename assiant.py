import speech_recognition
import pyttsx3
import webbrowser
from youtube_search import YoutubeSearch
import wikipedia
my_mic=speech_recognition.Microphone()
rec=speech_recognition.Recognizer()

#chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

def listen():
    print('Listening...')
    try:
        with my_mic as source:
            rec.adjust_for_ambient_noise(source)
            audio=rec.listen(source)
            grec=str(rec.recognize_google(audio))
        print(grec)
        return grec
    except Exception:
        print("Couldn't recognise what you just said")
        return "o"

engine=pyttsx3.init()
rate=engine.setProperty('rate', 175)
voices=engine.getProperty('voices')


#print(voices[1])


def speak(statement):
    for voice in voices:
        i=1
    engine.setProperty('voice', voice.id)
    print(statement)
    engine.say(statement)
    engine.runAndWait()

speak("""Welcome to Cisco Assistant
      What can I do""")



#while True:
query=listen()
query=query.lower()
if 'open youtube' in query:
    speak('Opening youtube')
    webbrowser.open('https://www.youtube.com')
elif query.startswith('search for'):
    searchMaterial = query.replace('search for', '')
    speak("Here are your search results")
    link = f'https://www.google.com/search?q={searchMaterial}'
    webbrowser.open(link)
elif query.startswith('search on youtube for'):
    youtubelink = query.replace('search on youtube for', '')
    speak("Here are the videos that match your query")
    webbrowser.open(f'https://www.youtube.com/results?search_query={youtubelink}')
elif query.startswith("play"):
    query = query.replace("play", "")
    result = YoutubeSearch(query, max_results=1).to_dict()
    result = result[0]["url_suffix"]
    vidLink = f"https://www.youtube.com{result}"
    webbrowser.open(vidLink)
elif query.startswith("give me information about"):
    query = query.replace('give me information about', "")
    info = wikipedia.summary(query, sentences=2)
    speak(info)
    

    
    
        
