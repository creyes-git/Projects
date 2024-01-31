import streamlit as st
import pandas as pd
import sqlite3 as sql

st.set_page_config(page_icon= "",page_title= "CreditHub", layout= "wide", initial_sidebar_state= "expanded")

connection = sql.connect("CreditHub\\DB\\Database.db")
cursor = connection.cursor()


Name = st.text_area("Enter the card name")
Category = st.selectbox("Choose the category", options=  ["Travel", "Cash Back", "0% APR", "Airline", "Business", "Hotel", "Balance Transfer", "Rewards"])
Welcome_Bonus = st.number_input("Enter the welcome bonus in Points", min_value= 0) 
Annual_Fee = st.number_input("Enter the annual fee", min_value= 0)
Recommended_Credit_Score = st.selectbox("Choose the recommended credit score range", options=["Bad (0-649)", "Fair (650-699)", "Good (700-749) ", "Excellent (750+)"])
Issuer_Name = st.text_area("Enter the name of the issuer")
Pros = st.text_area("Enter 3 PROS of the card separated by commas")
Cons =  st.text_area("Enter 3 CONS of the card separated by commas")

if st.button("Submit"):
    cursor.execute("INSERT INTO Cards VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (Issuer_Name, Name, Category, Welcome_Bonus, Annual_Fee, Recommended_Credit_Score, Pros, Cons))
    connection.commit()
    connection.close()