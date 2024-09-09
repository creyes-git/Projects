
from langchain_groq import ChatGroq as groq
from langchain_core.prompts import ChatPromptTemplate as template
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

def chat_groq(input):
    
    llm = groq(
        api_key=api_key,
        model = "llama-3.1-8b-instant",
        temperature = 0.55,
        max_tokens = 200,
        timeout = None,
        max_retries = 2)
    
    history = ""
    responses_history = ""

    prompt = f'''System Message: You are a assistant for a lights store named **Progressive Lighting**, you will help giving recommendations for customers based on product data that i will give,
        you will answer customer questions about the store, shipping time, store policy and more, you will take the chat history as conntext to answer the actual question...
        This is the context: {history}.'''


    response = llm.invoke(prompt + f"\n User: {input}")
    history += f"User: {input}\n"
    
    responses_history += f"{response.content}\n"
    history += f"AI Assistant: {response.content}\n"
    
    return f"{responses_history} \n {response.content}"
    