from modules.screenwriter import talk_with_screenwriter, clear_memory, memory
import streamlit as st
import os


st.set_page_config(page_title = "Hayek&You", page_icon = "🧑‍🏫", layout = "centered", initial_sidebar_state = "expanded")


def save_script():
        
    if os.path.exists(r"assets\temp\script.txt"):
        os.remove(r"assets\temp\script.txt")
        
    script = ""

    with open(r"assets\temp\script.txt", "w") as f:
        for msg in memory.messages:
            if msg.type == "ai":
                script = msg.content
        
        f.write(f"{script}")


with st.sidebar:

    new_chat = st.button(label = "New Chat", 
                         type = "primary", 
                         key = "new_chat", 
                         icon = "✍🏼",
                         use_container_width = True,
                         help = "Start a new chat and clear the conversation history")
    
    
    placeholder = st.empty()
    if memory.messages[-1].type == "ai":
        dowload_script = placeholder.download_button(label = "Get Script!", 
                                            type = "secondary", 
                                            key = "get_script", 
                                            data = open(r"assets\temp\script.txt"),
                                            icon = "📥",
                                            on_click = save_script,
                                            mime = "text/plain",
                                            use_container_width = True,
                                            help = "Get the last conversation messages as the final script")
        
    else:
        dowload_script = placeholder.download_button(label = "Get Script!", 
                                                     data = r"assets\temp\script.txt",
                                                     icon = "📥",
                                                     use_container_width = True,
                                                     disabled = True)
        
    
# Buttons actions        
if new_chat:
    clear_memory()


for msg in memory.messages:
    if msg.type == "human" or msg.type == "ai":
        st.chat_message(msg.type).write(msg.content)


with st.spinner("Thinking..."):
    if user_input := st.chat_input(placeholder = "Your message..."):
        
        st.chat_message("human").write(user_input)
        response = talk_with_screenwriter(user_input)
        st.chat_message("ai").write(response)