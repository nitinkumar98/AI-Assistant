#   to convert text to speech
import pyttsx3

#to recongnise the user sound
import speech_recognition as sr

# for date and time
import datetime

# to search the wikipedia
import wikipedia

# to open the web browser
import webbrowser

# to make the functionality into the os
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("Good morning")
    elif hour >=12 and hour <=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("hey  i am nitin and please tell me about you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=5)
        speak("According to Wikipedia")
        print(results)
        speak(results)


    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'play music' in query:
        music_dir = 'path to directory'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[4]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open sublime' in query:
        codePath  = "path to that app and use double  backslash(\\) in place of (\)"
        os.startfile(codePath)












