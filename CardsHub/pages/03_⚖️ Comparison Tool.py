import pandas as pd
import sqlite3 as sql
import streamlit as st
from PIL import Image
import requests
import colorama

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

# loading css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

connection = sql.connect("Cards.db")
cursor = connection.cursor()

#cards list
card_name_list = list()
for i in cursor.execute("SELECT name FROM cards").fetchall():
    card_name_list.append(i[0])
    
#rewards programs:
    

# columns
cc1, cc2, cc3, cc4 = st.columns(4)

with cc1:
    card1_name = st.selectbox(options= card_name_list, label= " ", index = 0)
    # Image
    st.image(Image.open(requests.get(cursor.execute("SELECT Image_URL FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0], stream=True).raw)) 
    # Category
    st.write(":red[**Category**]")
    st.image(Image.open(f"images/{cursor.execute('SELECT Category FROM cards WHERE name = ?', (card1_name,)).fetchall()[0][0]}.png"), width= 75)
    # Welcome bonus
    st.metric(":red[**Welcome bonus**]", str(cursor.execute("SELECT Welcome_Bonus FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0])+" Points")
    # Annual fee
    st.metric(":red[**Annual fee**]", str(cursor.execute("SELECT Annual_Fee FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0])+"$")
    # Rewards rate
    with st.expander(":red[**Card Rewards**]"):
        rewards = list(str(cursor.execute("SELECT Rewards_rate FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0]).split("."))
        for i in rewards:
            st.markdown(f"{i}")
    
    
    
    # Recommended credit score
    st.write(":red[**Recommended credit score**]")
    st.image(Image.open(f"images/{str(cursor.execute('SELECT Recommended_Credit_Score FROM cards WHERE name = ?', (card1_name,)).fetchall()[0][0]).strip()}.png"), width= 200)
    # Review
    st.text_area(":red[**Highlights**]", cursor.execute("SELECT Review FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0], height= 250)
    # Pros
    st.write(":red[**Pros**]")
    pros = cursor.execute("SELECT Pros FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0]
    lista = list(str(pros).split("\n"))
    for i in lista:
        st.write(f"- {i}")
    #Cons
    st.write(":red[**Cons**]")
    cons = cursor.execute("SELECT Cons FROM cards WHERE name = ?", (card1_name,)).fetchall()[0][0]
    lista = list(str(cons).split("\n"))
    for i in lista:
        st.write(f"- {i}")
        
with cc4:
    card2_name = st.selectbox(options= card_name_list, label= "  ", index = 2)
    st.image(Image.open(requests.get(cursor.execute("SELECT Image_URL FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0], stream=True).raw)) 
    # Category
    st.write(":blue[**Category**]")
    st.image(Image.open(f"images/{cursor.execute('SELECT Category FROM cards WHERE name = ?', (card2_name,)).fetchall()[0][0]}.png"), width= 75)
    # Welcome bonus
    st.metric(":blue[**Welcome bonus**]", str(cursor.execute("SELECT Welcome_Bonus FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0])+" Points")
    # Annual fee
    st.metric(":blue[**Annual fee**]", str(cursor.execute("SELECT Annual_Fee FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0])+"$")
    # Rewards rate
    st.text_area(":blue[**Card Rewards**]",(cursor.execute("SELECT Rewards_rate FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0]), height= 300)
    # Recommended credit score
    st.write(":blue[**Recommended credit score**]")
    st.image(Image.open(f"images/{str(cursor.execute('SELECT Recommended_Credit_Score FROM cards WHERE name = ?', (card2_name,)).fetchall()[0][0]).strip()}.png"), width= 200)
    # Review
    st.text_area(":blue[**Highlights**]", cursor.execute("SELECT Review FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0], height= 250)
    # Pros
    st.write(":blue[**Pros**]")
    pros = cursor.execute("SELECT Pros FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0]
    lista = list(str(pros).split("\n"))
    for i in lista:
        st.write(f"- {i}")
    #Cons
    st.write(":blue[**Cons**]")
    cons = cursor.execute("SELECT Cons FROM cards WHERE name = ?", (card2_name,)).fetchall()[0][0]
    lista = list(str(cons).split("\n"))
    for i in lista:
        st.write(f"- {i}")

local_css('style.css')