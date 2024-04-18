import streamlit as st
from streamlit_lottie import st_lottie
import sqlite3 as sql
import pandas as pd
from PIL import Image
import requests
import json

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

connection = sql.connect("Cards.db")
cursor = connection.cursor()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

cc1, cc2,cc3 = st.columns(3)
with cc2:
    st_lottie(load_lottiefile("images/match.json"), height = 200, quality = "high")
    st.warning("Fill the form and get a card recommendation")
    
# Card match form
with st.form(key="card_match_form", clear_on_submit= True) as form:
    points = 0
    
    goal = st.radio("What are you looking for in a card? ", ("Getting cash back","Earning travel rewards", "Paying business expenses", "Building credit history", "Other"))
    credit_score = st.number_input("What is your credit score? ", min_value=0, max_value=850, step=10)
    credit_history = st.number_input("How many years had your credit history? ", min_value=0, max_value = 100, step=1)
    employment = st.radio("What is your employment status? ", ("Employed", "Unemployed", "Self-employed", "Retired", "Student"))
    income = st.number_input("What is your anual income? ", min_value=0, step = 1000)
    rent_mortgage = st.number_input("What is your monthly rent or mortgage? ", min_value=0, step = 100)
    bank = st.radio("What kind of bank account do you have? ", ("Checking", "Savings", "None", "Both"))
    
    submit = st.form_submit_button(":rainbow[**Match**]")

# Calculate points:
if submit:
    # income
    if income >= 20000:
        points += 1
    elif income >= 50000:
        points += 2
    elif income >= 100000:
        points += 3
    elif income >= 200000:
        points += 4
    else:
        points += -1
        
    # rent
    if rent_mortgage >= 1000:
        points += -0.5
    elif rent_mortgage >= 2000:
        points += -1
    elif rent_mortgage >= 3000:
        points += -1.5
    elif rent_mortgage >= 5000:
        points += -2
        
    # credit score
    if credit_score >= 670:
        points += 1
    elif credit_score >= 700:
        points += 2
    elif credit_score >= 740:
        points += 3
    elif credit_score >= 800:
        points += 4
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
    if points >= 2:
        value = 95
    elif points >= 4:
        value = 250
    elif points >= 7:
        value = 550
    elif points >= 9:
        value = 1000
    else:
        value = 0
    
    # Dataframe
    if goal == "Getting cash back":
        df = pd.DataFrame(cursor.execute(f"SELECT * FROM cards WHERE Annual_Fee <= {value} and Category = 'Cash Back' or Category = 'Store'"), columns=[i[0] for i in cursor.description]).sort_values(by="Annual_Fee", ascending=False).head(5)
    elif goal == "Earning travel rewards":
        df = pd.DataFrame(cursor.execute(f"SELECT * FROM cards WHERE Annual_Fee <= {value} and Category = 'Travel' or Category = 'Hotel'"), columns=[i[0] for i in cursor.description]).sort_values(by="Annual_Fee", ascending=False).head(5)
    elif goal == "Paying business expenses":
        df = pd.DataFrame(cursor.execute(f"SELECT * FROM cards WHERE Annual_Fee <= {value} and Category = 'Business' or Category = 'Store'"), columns=[i[0] for i in cursor.description]).sort_values(by="Annual_Fee", ascending=False).head(5)
    elif goal == "Building credit history":
        df = pd.DataFrame(cursor.execute(f"SELECT * FROM cards WHERE Annual_Fee <= {value} and Category = 'Secured' or Category = 'Student'"), columns=[i[0] for i in cursor.description]).sort_values(by="Annual_Fee", ascending=False).head(5)
    else:
        df = pd.DataFrame(cursor.execute(f"SELECT * FROM cards WHERE Annual_Fee <= {value}"), columns=[i[0] for i in cursor.description]).sort_values(by="Annual_Fee", ascending=False).head(5)
    
    # Printing all cards
    for i in df.values:
        with st.container():
            c1, c2, c3, c4 = st.columns(4)
                
            with c1.container():
                c1.write(f"**{i[1]}**")
                c1.image(Image.open(requests.get(i[-1], stream=True).raw))
            
            with c2.container():
                c2.write("**Annual Fee:**")
                c2.markdown(f"{i[5]}$")
                c2.write("**Welcome Bonus:**")
                c2.markdown(f"{i[4]} Points")
                c2.write("**Recommended Credit Score:**")
                c2.markdown(i[6])
                
            with c3.container():
                c3.write("**Category:**")
                c3.image(Image.open(f"images/{i[2]}.png"), width= 100, clamp=True)
    
            with c4.container():
                c4.write("**Highlights:**")
                c4.markdown(f"{i[9]}")
            

            st.markdown("---")
            
                
           