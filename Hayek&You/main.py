from hayek_agent import *
import streamlit as st
from PIL import Image

st.set_page_config(page_title = "Hayek&You", page_icon="🧑‍🏫", layout = "centered", initial_sidebar_state = "expanded")


with st.sidebar:
    
    st.image(Image.open("Hayek&You/images/mini_hayek.png"), use_column_width = True)