from hayek_agent import ask_to_hayek, clear_memory, memory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
import streamlit as st
from PIL import Image


st.set_page_config(page_title = "Hayek&You", page_icon="🧑‍🏫", layout = "centered", initial_sidebar_state = "expanded")


with st.sidebar:
    
    st.image(Image.open("Hayek&You/images/mini_hayek.png"), use_column_width = True)
    
    new_chat = st.button(label = "New Chat", 
                         type = "primary", 
                         key = "new_chat", 
                         use_container_width = True,
                         help = "Start a new chat and clear the conversation history")
    
        
if new_chat:
    clear_memory()


for msg in memory.messages[1:]:
    
    st.chat_message(msg.type).write(msg.content)


if user_input := st.chat_input(placeholder = "Ask me anything about economy"):
    
    st.chat_message("human").write(user_input)
    response = ask_to_hayek(user_input)
    st.chat_message("ai").write(response)
