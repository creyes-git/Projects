import pandas as pd
import sqlite3 as sql
import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

connection = sql.connect("Cards.db")
cursor = connection.cursor()

# functions:
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

c1, c2,c3 = st.columns(3)
with c2:
    st_lottie(load_lottiefile("images/lottie1.json"), height = 111, quality = "high")
    st.warning("Enter the details of the card you want to add")

# card form:
with st.form(key="card_form", clear_on_submit= True) as card_form:
    Issuer_Name = st.selectbox("Select the issuer", options=  ["Discover", "Chase", "Bank of America","Wells Fargo","Citi", "Capital One", "Credit One Bank", "American Express","U.S. Bank","VISA", "Mastercard"])
    Name = st.text_input("Enter the card name")
    Category = st.selectbox("Choose the category", options=  ["Travel","Cash Back","Store","Hotel","Student","Secured", "Business", "Balance Transfer", "Other"])
    Top_rewards_rate = st.text_area("Enter the top rewards rate")
    Welcome_Bonus = st.number_input("Enter the welcome bonus in dollars", min_value= 0) 
    Annual_Fee = st.number_input("Enter the annual fee", min_value= 0)
    Recommended_Credit_Score = st.selectbox("Choose the recommended credit score range", options=["Bad (0-649)", "Fair (650-699)", "Good (700-749)", "Excellent (750+)"])
    Pros = st.text_area("Enter 3 PROS of the card separated by line breaks")
    Cons =  st.text_area("Enter 3 CONS of the card separated by line breaks")
    Review = st.text_area("Enter a review of the card")
    Image_URL = st.text_input("Enter the URL of the card image")

    # submit button, save cards data:
    if st.form_submit_button(":rainbow[**Submit**]"):
        if cursor.execute(f"SELECT Name FROM cards where Name = '{Name}'").fetchone():
            st.warning("Card already exists", icon= "⚠️")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS cards (Issuer_Name, Name, Category, Rewards_rate, Welcome_Bonus, Annual_Fee, Recommended_Credit_Score, Pros, Cons, Review, Image_URL)")  
            cursor.execute("INSERT INTO cards VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Issuer_Name.strip(), Name.strip(), Category.strip(), Top_rewards_rate.strip(), Welcome_Bonus, Annual_Fee, Recommended_Credit_Score.strip(), Pros.strip(), Cons.strip(), Review.strip(), Image_URL.strip()))
            connection.commit()
            st.success("Card added successfully", icon= "✅")