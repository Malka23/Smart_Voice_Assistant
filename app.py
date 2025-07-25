import streamlit as st
from voice_assistant import take_command, run_assistant

st.set_page_config(page_title="Smart Voice Assistant")
st.title("🎙️ Smart Voice Assistant")

if st.button("Start Listening"):
    command = take_command()
    if command:
        st.markdown(f"**You said:** `{command}`")
        response = run_assistant(command)
        st.markdown(f"**Assistant:** {response}")
    else:
        st.warning("No recognizable command detected.")
