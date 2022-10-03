import speech_recognition
import pyttsx3
import webbrowser
my_mic=speech_recognition.Microphone()
rec=speech_recognition.Recognizer()

def listen():
    print('Listening...')
    with my_mic as source:
        audio=rec.listen(source)
        grec=str(rec.recognize_google(audio))
    print(grec)
    return grec

engine=pyttsx3.init()
rate=engine.setProperty('rate', 175)
voices=engine.getProperty('voices')
#engine.setProperty('voices', voices[0].id)

#print(voices[1])


def speak(statement):
    engine.say(statement)
    print(statement)
    engine.runAndWait()
    engine.stop()

speak("""Welcome to Cisco Assisstant
      What can I do""")

for voice in voices:
    i=1
engine.setProperty('i', voice.id)
print(voice)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


#while True:
query=listen()
    
        
