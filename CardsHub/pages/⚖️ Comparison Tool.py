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
cc1, cc2, cc3 = st.columns(3)

with cc1:
    st.write('<span class="icon type-text1">Card 1</span>',unsafe_allow_html=True)
    card1_name = st.selectbox(options= card_name_list, label= " ")
    # Image
    st.image(Image.open(requests.get(cursor.execute("SELECT Image_URL FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0], stream=True).raw)) 
    # Category
    st.write(":red[**Category**]")
    st.image(Image.open(f"images/{cursor.execute('SELECT Category FROM cards WHERE name = ?', (card1_name,)).fetchall()[0][0]}.png"), width= 75)
    # Rewards rate
    st.text_area(":red[**Rewards rate**]",(cursor.execute("SELECT Rewards_rate FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0]), height= 200)
    # Welcome bonus
    st.metric(":red[**Welcome bonus**]", str(cursor.execute("SELECT Welcome_Bonus FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0])+"$")
    # Annual fee
    st.metric(":red[**Annual fee**]", str(cursor.execute("SELECT Annual_Fee FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0])+"$")
    # Recommended credit score
    st.write(":red[**Recommended credit score**]")
    st.image(Image.open(f"images/{str(cursor.execute('SELECT Recommended_Credit_Score FROM cards WHERE name = ?', (card1_name,)).fetchall()[0][0]).strip()}.png"), width= 55)
    # Review
    st.text_area(":red[**Review**]", cursor.execute("SELECT Review FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0], height= 300)
    # Pros and Cons
    with st.container():
        st.write(":red[**Pros**]")
        st.write(cursor.execute("SELECT Pros FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0])
        st.write(":red[**Cons**]")
        st.write(cursor.execute("SELECT Cons FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0])
         
with cc3:
    st.write('<span class="icon type-text2">Card 2</span>',unsafe_allow_html=True)
    card2_name = st.selectbox(options= card_name_list, label= "  ")
    st.image(Image.open(requests.get(cursor.execute("SELECT Image_URL FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0], stream=True).raw)) 
    # Category
    st.write(":blue[**Category**]")
    st.image(Image.open(f"images/{cursor.execute('SELECT Category FROM cards WHERE name = ?', (card2_name,)).fetchall()[0][0]}.png"), width= 75)
    # Rewards rate
    st.text_area(":blue[**Rewards rate**]",(cursor.execute("SELECT Rewards_rate FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0]), height= 200)
    # Welcome bonus
    st.metric(":blue[**Welcome bonus**]", str(cursor.execute("SELECT Welcome_Bonus FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0])+"$")
    # Annual fee
    st.metric(":blue[**Annual fee**]", str(cursor.execute("SELECT Annual_Fee FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0])+"$")
    # Recommended credit score
    st.write(":blue[**Recommended credit score**]")
    st.image(Image.open(f"images/{str(cursor.execute('SELECT Recommended_Credit_Score FROM cards WHERE name = ?', (card2_name,)).fetchall()[0][0]).strip()}.png"), use_column_width= True)
    # Review
    st.text_area(":blue[**Review**]", cursor.execute("SELECT Review FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0], height= 300)
    # Pros and Cons
    with st.container():
        st.write(":blue[**Pros**]")
        st.write(cursor.execute("SELECT Pros FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0])
        st.write(":blue[**Cons**]")
        st.write(cursor.execute("SELECT Cons FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0]) 
                
with cc2:
    with st.container():
        for i in range(3):
            st.write("  ")
        st.image(Image.open("images/versus.png"), use_column_width= True)
            
local_css('style.css')