import streamlit as st
import sqlite3 as sql
from PIL import Image

# Connect to the SQLite database containing credit card data
connection = sql.connect("Cards.db")
cursor = connection.cursor()

c1, c2, c3 = st.columns(3)
c2.image(Image.open("images/scanner.png"), width = 150, clamp=True)

# Card match form
with st.form(key="card_match_form", clear_on_submit= True) as form:
    goal = st.selectbox("What are you looking for in a card? ", ("Getting cash back","Earning travel rewards","Transferring a balance",
                        "Saving money on interest", "Paying business expenses", "Building credit history", "Repairing credit" ))
    employment = st.selectbox("What is your employment status? ", ("Employed", "Unemployed", "Self-employed", "Retired", "Student", "Other"))
    
    income = st.number_input("What is your anual income? ", min_value=0)
    
    rent_mortgage = st.number_input("What is your monthly rent or mortgage? ", min_value=0)
    
    credit_history = st.number_input("How many months had you credit history? ", min_value=0)
    
    credit_score = st.number_input("What is your credit score? ", min_value=0, max_value=850, step=1)
    
    bank = st.checkbox("What kind of bank account do you have? ")