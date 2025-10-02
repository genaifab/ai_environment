import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Test Flight")

prompt = st.text_input("Enter a message for the AI:")

if st.button("Send"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    st.write(response.choices[0].message.content)