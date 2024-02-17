import pandas as pd
import sqlite3 as sql
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json
import requests

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


#cards list
card_name_list = list()
for i in cursor.execute("SELECT name FROM cards").fetchall():
    card_name_list.append(i[0])

# columns
c1, c2,c3 = st.columns(3)
cc1, cc2, cc3 = st.columns(3)

with c2:
    st_lottie(load_lottiefile("images/lottie2.json"), height = 200, quality = "high")


with cc1:
    st.write('<span class="icon type-text2">Card 1</span>',unsafe_allow_html=True)
    card1_name = st.selectbox(options= card_name_list, label= "Select Card 1")
    # Image
    st.image(Image.open(requests.get(cursor.execute("SELECT Image_URL FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0], stream=True).raw)) 
    # Category
    st.text("Category")
    st.image(Image.open(f"images/{cursor.execute('SELECT Category FROM cards WHERE name = ?', (card1_name,)).fetchall()[0][0]}.png"), width= 50)
    # Review
    st.text_area("Review", cursor.execute("SELECT Review FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0], height= 300)
            
with cc3:
    st.write('<span class="icon type-text3">Card 2</span>',unsafe_allow_html=True)
    card2_name = st.selectbox(options= card_name_list, label= "Select Card 2")
    st.image(Image.open(requests.get(cursor.execute("SELECT Image_URL FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0], stream=True).raw)) 
    
    
                
with cc2:
    for i in range(7):
        st.write("  ")
        
    st.image(Image.open("images/vs.png"), width= 185,use_column_width= True, clamp= True)
        
local_css('style.css')