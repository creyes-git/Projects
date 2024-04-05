import streamlit as st
import sqlite3 as sql
import pandas as pd
from PIL import Image
import requests

# Connect to the SQLite database containing credit card data
connection = sql.connect("Cards.db")
cursor = connection.cursor()

c1, c2, c3 = st.columns(3)
c2.image(Image.open("images/scanner.png"), width = 150, clamp=True)

# Card match form
with st.form(key="card_match_form", clear_on_submit= True) as form:
    
    points = 0
    
    goal = st.selectbox("What are you looking for in a card? ", ("Getting cash back","Earning travel rewards", "Paying business expenses", "Building credit history"))
    
    employment = st.selectbox("What is your employment status? ", ("Employed", "Unemployed", "Self-employed", "Retired", "Student", "Other"))
    
    income = st.number_input("What is your anual income? ", min_value=0)
    
    rent_mortgage = st.number_input("What is your monthly rent or mortgage? ", min_value=0)
    
    credit_history = st.number_input("How many years had you credit history? ", min_value=0, max_value = 100, step=1)
    
    credit_score = st.number_input("What is your credit score? ", min_value=0, max_value=850, step=1)
    
    bank = st.radio("What kind of bank account do you have? ", ("Checking", "Savings", "None", "Both"))
    
    
    submit = st.form_submit_button(":rainbow[**Submit**]")


if submit:
    # Calculate points:
        # employment
        if employment == "Employed" or employment == "Self-employed":
            points += 1
        elif employment == "Unemployed":
            points += -1
        # income
        if income >= 20000:
            points += 1
        elif income >= 50000:
            points += 2
        elif income >= 100000:
            points += 3
        elif income >= 250000:
            points += 5
        else:
            points += -1
        # rent
        if rent_mortgage >= 1500:
            points += -0.5
        elif rent_mortgage >= 3000:
            points += -1
        elif rent_mortgage >= 5000:
            points += -1.5
        else:
            points += +1
        # credit score
        if credit_score >= 700:
            points += 2
        elif credit_score >= 750:
            points += 3
        elif credit_score >= 800:
            points += 5
        else:
            points += -1
        # credit history
        if credit_history >= 1:
            points += 0.5
        if credit_history >= 2:
            points += 1
        if credit_history >= 5:
            points += 2
        if credit_history >= 10:
            points += 3
        else:
            points += -1
        
        # POINTS
        if points > 2:
            value = 95
        elif points > 4:
            value = 250
        elif points > 6:
            value = 500
        elif points > 8:
            value = 700
        else:
            value = 0
            
        df = pd.DataFrame(cursor.execute(f"SELECT * FROM cards WHERE Annual_Fee <= {value}"), columns=[i[0] for i in cursor.description]).sort_values(by="Annual_Fee", ascending=False).head(5)
        
        # Printing all cards
        for i in df.values:
            with st.container():
                c1, c2, c3 = st.columns(3)
                
                with c1.container():
                    c1.write(f"**{i[1]}:**")
                    c1.image(Image.open(requests.get(i[-1], stream=True).raw))
                    c1.write("**Category:**")
                    c1.image(Image.open(f"images/{i[2]}.png"), width= 55, clamp=True)
    
                with c2.container():
                    c2.markdown("**Rewards:**")
                    c2.markdown(i[3])
                    
                with c3.container():
                    c3.write("**Annual Fee:**")
                    c3.markdown(f"{i[5]}$")
                    c3.write("**Welcome Bonus:**")
                    c3.markdown(f"{i[4]}$")
                    c3.write("**Recommended Credit Score:**")
                    c3.markdown(i[6])

                st.markdown("---")
        
                
           