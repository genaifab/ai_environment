# chat_connect.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Send a simple request
response = client.chat.completions.create(
    model="gpt-4o-mini",  # you can also use gpt-4.1, gpt-4o, etc.
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who has won the most olympic gold medals?"}
    ],
)

# Print the response
print("AI says:", response.choices[0].message.content)