import streamlit as st
import pandas as pd
import sqlite3 as sql

with st.sidebar:
    st.write("## CardsHub")
    
st.set_page_config(page_icon= ":credit_card:",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

connection = sql.connect("CardsHub\\Cards.db")
cursor = connection.cursor()



st.title("Fill card details on the form below:")


with st.form(key="card_form", clear_on_submit= True):
    Issuer_Name = st.selectbox("Select the issuer", options=  ["Discover", "Chase", "Bank of America","Wells Fargo","Citi", "Capital One", "Credit One Bank", "American Express", "VISA", "Mastercard"])
    Name = st.text_area("Enter the card name")
    Category = st.selectbox("Choose the category", options=  ["Travel", "Cash Back", "0% APR","Student","Secured", "Business", "Balance Transfer", "Rewards"])
    Rewards_rate = st.text_area("Enter the rewards rate")
    Welcome_Bonus = st.number_input("Enter the welcome bonus in dollars", min_value= 0) 
    Annual_Fee = st.number_input("Enter the annual fee", min_value= 0)
    Recommended_Credit_Score = st.selectbox("Choose the recommended credit score range", options=["Bad (0-649)", "Fair (650-699)", "Good (700-749) ", "Excellent (750+)"])
    Pros = st.text_area("Enter 3 PROS of the card separated by line breaks")
    Cons =  st.text_area("Enter 3 CONS of the card separated by line breaks")
    Image_URL = st.text_input("Enter the URL of the card image")
    
    boton = st.form_submit_button("Submit Card")
    

    if boton:
        cursor.execute("CREATE TABLE IF NOT EXISTS Cards(Issuer_Name TEXT, Name TEXT, Rewards_rate TEXT, Category TEXT, Welcome_Bonus INTEGER, Annual_Fee INTEGER, Recommended_Credit_Score TEXT, Pros TEXT, Cons TEXT, Image_URL TEXT)")
        cursor.execute("INSERT INTO Cards VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Issuer_Name, Name, Category, Rewards_rate, Welcome_Bonus, Annual_Fee, Recommended_Credit_Score, Pros, Cons, Image_URL))
        st.success("Your card has been submitted!")
        connection.commit()
        connection.close()

if st.button("View Cards"):
    st.table(cursor.execute("SELECT * FROM Cards"))
    connection.commit()
    connection.close()
    
if st.button("Delete Cards"):
    cursor.execute("DELETE FROM Cards")
    st.success("All cards have been deleted!")
    connection.commit()
    connection.close()