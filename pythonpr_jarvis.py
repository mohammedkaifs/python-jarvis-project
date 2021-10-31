import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

from wikipedia.wikipedia import summary

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good evening")

    speak("I am jarvis sir, please tell me how may i help you")
    speak("ooh kaif bhai")
def takeCommand():
    # It take microphone input from the user and returns string output

    r =sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing....")    
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:

        print("say that again please...")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("Google.com")
        
       
            # content = takeCommand()

        elif 'play music' in query:
            music_dir='C:\\Users\\Dell\\Music\\Favorite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)