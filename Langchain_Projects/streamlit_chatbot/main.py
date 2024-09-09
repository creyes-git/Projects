import pandas as pd
import streamlit as st
from langchain_groq import ChatGroq as groq
from langchain_core.prompts import ChatPromptTemplate as template
from dotenv import load_dotenv
import os


st.set_page_config(page_icon= ":robot:",page_title= "Groq Chatbot", layout= "centered", initial_sidebar_state= "expanded")

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = groq(
    api_key=api_key,
    model = "llama-3.1-8b-instant",
    temperature = 0.55,
    max_tokens = 200,
    timeout = None,
    max_retries = 2)





prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)

input = st.chat_input("User: ")


if input:
   
    response = llm.invoke(input)

    st.write(response.content)