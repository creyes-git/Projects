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
    Issuer_Name = st.selectbox("Select the issuer", options=  ["Discover", "Chase", "Bank Of America", "Wells Fargo", "Citi", "Capital One", "Credit One Bank", "American Express","U.S. Bank", "Penfed", "Other"])
    Name = st.text_input("Enter the card name")
    Category = st.selectbox("Choose the category", options=  ["Travel","Cash Back","Store","Hotel","Secured", "Business", "Balance Transfer", "Other"])
    Multipliers = st.text_area("Enter the card Multipliers separated by line breaks")
    All_benefits = st.text_area("Enter other benefits of the card separated by line breaks, like travel credits, etc.")
    Welcome_Bonus = st.number_input("Enter the welcome bonus in POINTS",help = "If the welcome bonus is a cash bonus offer, consider it as 100 points per dollar", min_value= 0) 
    Welcome_Bonus_Requirements = st.number_input("Enter the welcome bonus offer spending requirements($)", min_value = 0)
    Annual_Fee = st.number_input("Enter the annual fee($)", min_value = 0)
    APR = st.text_input("Enter the APR range")
    Recommended_Credit_Score = st.selectbox("Choose the recommended credit score range", options=["No Credit Nedded", "580-850", "670-850", "740-850"])
    Pros = st.text_area("Enter the PROS of the card separated by line breaks")
    Cons =  st.text_area("Enter the CONS of the card separated by line breaks")
    Why_Get = st.text_area("Enter highlights of the card, or why you should get this card")
    Image_URL = st.text_input("Enter the URL of the card image")

    # submit button, save cards data:
    if st.form_submit_button(":rainbow[**Submit**]"):
        cursor.execute("CREATE TABLE IF NOT EXISTS cards (Issuer_Name,Card_Name,Card_Image,Category,Multipliers,Signup_Bonus_Requirement,Signup_Bonus,Annual_Fee,APR_Range,Recommended_Score,Why_Get,Pros,Cons,All_Benefits)")  
        
        if cursor.execute(f"SELECT Card_Name FROM cards where Card_Name = '{Name.strip()}'").fetchone():
            st.warning("Card already exists", icon= "⚠️")
        else:
            cursor.execute("INSERT INTO cards VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Issuer_Name.strip(), Name.strip(), Image_URL.strip(), Category.strip(), Multipliers.strip(), Welcome_Bonus_Requirements, Welcome_Bonus, Annual_Fee, APR.strip(), Recommended_Credit_Score.strip(), Why_Get.strip(), Pros.strip(), Cons.strip(), All_benefits.strip()))
            connection.commit()
            st.success("Card added successfully", icon= "✅")