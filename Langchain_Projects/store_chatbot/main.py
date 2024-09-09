from groq_chat import chat_groq
import streamlit as st


st.set_page_config(page_icon= "🤖",page_title= "Groq Chatbot", layout= "centered", initial_sidebar_state= "expanded")

input = st.chat_input("User: ")

if input:
    
    with st.chat_message("user"):
        st.markdown(input)
    
    with st.chat_message("assistant"):
        st.write(chat_groq(input))