import streamlit as st
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os

# Initialize Streamlit App
st.set_page_config(page_title="Ashu Assistant", layout="centered")

# Header
st.title("🗣️ Ashu - Your AI Assistant")
st.write("Type your command below and I'll do my best to help you!")

# Handle user input
user_input = st.text_input("You:", "")

# Process the command
def run_ashu(command):
    response = ""

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        response = f"The current time is {time}"

    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        try:
            info = wikipedia.summary(person, sentences=2)
            response = info
        except:
            response = "Sorry, I couldn't find information on that person."

    elif 'play' in command:
        song = command.replace('play', '').strip()
        response = f"Playing {song} on YouTube..."
        pywhatkit.playonyt(song)

    elif 'search' in command:
        query = command.replace('search', '').strip()
        url = f"https://www.google.com/search?q={query}"
        response = f"Searching for {query}..."
        webbrowser.open_new_tab(url)

    elif 'open notepad' in command:
        response = "Opening Notepad... (Only works locally)"
        os.system('notepad')  # Will only work in local environment

    elif 'stop' in command or 'exit' in command:
        response = "Goodbye!"
    else:
        response = "I didn’t understand that. Try another command."

    return response

# Display output
if user_input:
    output = run_ashu(user_input.lower())
    st.markdown(f"**Ashu:** {output}")
