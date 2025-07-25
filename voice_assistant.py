import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os
import threading

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"User: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

def run_assistant(command):
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        response = f"The current time is {time}"
        speak(response)
        return response

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, sentences=2)
        speak(info)
        return info

    elif 'play' in command:
        song = command.replace('play', '')
        response = f"Playing {song}"
        speak(response)
        pywhatkit.playonyt(song)
        return response

    elif 'search' in command:
        query = command.replace('search', '')
        url = f"https://www.google.com/search?q={query}"
        response = f"Searching for {query}"
        speak(response)
        os.system(f'start {url}')  # For Windows
        return response

    elif 'open notepad' in command:
        os.system('notepad')
        speak("Opening Notepad")
        return "Opening Notepad"

    elif 'stop' in command or 'exit' in command:
        speak("Goodbye!")
        return "Goodbye!"

    else:
        response = "I didn’t understand that."
        speak(response)
        return response
