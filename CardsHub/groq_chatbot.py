from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api = os.getenv("GROQ_API_KEY")

llm = Groq(api_key=api)

response = llm.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user",
            "content": promt}
    ],
    temperature=1,
    max_tokens=100,
    stream=False)