import sqlite3 as sql
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

connection = sql.connect("Cards.db")
cursor = connection.cursor()

st.title(":red[**Credit Card**] :green[**Interest Calculator**]")

def calc_interest(balance, apr, days_billing_period):
    interest = balance * (apr / 100) * (days_billing_period / 365)
    return interest


with st.form(key="interest_form", clear_on_submit= True):
    st.warning("Enter the balance on the card, the interest rate and the number of days in the statement cycle and Calculate.")
    
    c1,c2,c3 = st.columns(3)
    
    balance = c1.number_input("Balance: ", min_value=0, help = "Use our Average Daily Balance Tool (also on this page) for the most accurate results. For a ballpark result, use the balance on your statement or an estimate. ")
    apr = c2.number_input("APR: ", help = "Enter the purchase APR listed on your statement. Enter as a decimal figure, such as 16.99 or 14.24.")
    days_billing_period = c3.selectbox("Days in billing period: ", options = [28,29,30,31], index = 2, help = "A billing period can have 28-31 days, depending on the month. Not sure? Use 30 as a default, or use the number of days in the month in which the billing period started. ")
    
    Calculate = st.form_submit_button(":green[**Calculate**]")
    c1.write("---")  
    
if Calculate:
    interest = calc_interest(balance, apr, days_billing_period)
    st.metric("- CHARGE FOR THIS STATEMENT CYCLE", f"${round(interest,2)}")