from modules.voice_actor import deepgram_text_to_speech
import streamlit as st


st.set_page_config(page_title = "Hayek&You", page_icon = "🧑‍🏫", layout = "centered", initial_sidebar_state = "expanded")


with st.sidebar:

    new_chat = st.button(label = "New Chat", 
                         type = "primary", 
                         key = "new_chat", 
                         use_container_width = True,
                         help = "Start a new chat and clear the conversation history")
    
        
if new_chat:
    clear_memory()


for msg in memory.messages:
    if msg.type == "human" or msg.type == "ai":
        st.chat_message(msg.type).write(msg.content)


if user_input := st.chat_input(placeholder = "Your message..."):
    
    st.chat_message("human").write(user_input)
    response = talk_with_screenwriter(user_input)
    st.chat_message("ai").write(response)