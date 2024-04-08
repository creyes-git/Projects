import streamlit as st
from streamlit_lottie import st_lottie
import sqlite3 as sql
import pandas as pd
import plotly.express as px
from PIL import Image
import requests
import json


connection = sql.connect("Cards.db")
cursor = connection.cursor()

# functions:
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

cc1, cc2,cc3 = st.columns(3)
with cc2:
    st_lottie(load_lottiefile("images/lottie3.json"), height = 200, quality = "high")
    card = st.selectbox(" **Select the card for more details about it:** 👇", options=  [i[0] for i in cursor.execute("SELECT name FROM cards")])

c1, c2 = st.columns(2)
c1.image(Image.open(requests.get(cursor.execute("SELECT Image_URL FROM cards WHERE name = ?", (card,)).fetchall()[0][0], stream=True).raw)) 
    # Category
c1.write(":blue[**Category**]")
c1.image(Image.open(f"images/{cursor.execute('SELECT Category FROM cards WHERE name = ?', (card,)).fetchall()[0][0]}.png"), width= 75)
    # Rewards rate
c2.text_area(":blue[**Rewards rate**]",(cursor.execute("SELECT Rewards_rate FROM cards WHERE name = ?", (card,)).fetchall()[0][0]), height= 200)
    # Welcome bonus
c2.metric(":blue[**Welcome bonus**]", str(cursor.execute("SELECT Welcome_Bonus FROM cards WHERE name = ?", (card,)).fetchall()[0][0])+"$")
    # Annual fee
c1.metric(":blue[**Annual fee**]", str(cursor.execute("SELECT Annual_Fee FROM cards WHERE name = ?", (card,)).fetchall()[0][0])+"$")
    # Recommended credit score
c1.write(":blue[**Recommended credit score**]")
c1.image(Image.open(f"images/{str(cursor.execute('SELECT Recommended_Credit_Score FROM cards WHERE name = ?', (card,)).fetchall()[0][0]).strip()}.png"), width= 200)
    # Review
c2.text_area(":blue[**Review**]", cursor.execute("SELECT Review FROM cards WHERE name = ?", (card,)).fetchall()[0][0], height= 300)
    # Pros and Cons
with c2.container():
    st.write(":blue[**Pros**]")
    st.write(cursor.execute("SELECT Pros FROM cards WHERE name = ?", (card,)).fetchall()[0][0])
    st.write(":blue[**Cons**]")
    st.write(cursor.execute("SELECT Cons FROM cards WHERE name = ?", (card,)).fetchall()[0][0]) 
 