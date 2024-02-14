import pandas as pd
import sqlite3 as sql
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")


connection = sql.connect("Cards.db")
cursor = connection.cursor()


# css file loading
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# load lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


st_lottie(load_lottiefile("lottie1.json"), height = 60, quality = "high")

card_name_list = cursor.execute("SELECT name FROM cards").fetchall()[0]


c1,c2,c3 = st.columns(3)

    
with c1:
    st.write('<span class="icon type-text2">Card 1</span>',unsafe_allow_html=True)
    #card1_name = st.selectbox(options= card_name_list)
    
with c2:
    st.write('<span class="icon type-text3">Card 2</span>',unsafe_allow_html=True)
    
with c3:
    st.write('<span class="icon type-text1">Card 3</span>',unsafe_allow_html=True)
        
        
local_css('style.css')