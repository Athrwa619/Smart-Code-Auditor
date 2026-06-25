import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load the secret API key from the .env file (Industry Standard!)
load_dotenv()

# 2. Initialize the Groq client (Hire the "Waiter")
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 3. Give the Waiter an order to take to LLaMA 3.1
response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Hi LLaMA, give me a 1-sentence greeting for Athrwa!"}],
    model="llama-3.1-8b-instant",
)

# 4. Print the AI's reply
print("\n🤖 AI Says:", response.choices[0].message.content, "\n")
