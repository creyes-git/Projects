import sqlite3 as sql
import streamlit as st
import pandas as pd
import json

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

connection = sql.connect("Cards.db")
cursor = connection.cursor()


st.title(":red[Balance tran]:green[sfer calculator]")

with st.form(key="balance_transfer_form", clear_on_submit= True):
    st.warning("Transferring debt to a credit card with a 0% introductory annual percentage rate, or APR, could save you hundreds of dollars in interest while you pay down your debt.")
    c1, c2 = st.columns(2)
    
    c1.write("Debt you want to transfer to the new card")
    debt =c1.number_input("  ", min_value = 0)
   
    c1.write("Balance transfer fee on new card")
    fee = c1.selectbox(" ", ["0%", "1%", "2%", "3%", "4%", "5%"], index = 0)
    
    c2.write("Interest rate charged on that current debt")
    apr = c2.number_input("", min_value=0, help="Do not include percent sign. For example, 15% would be ''15,'' while 14.25% would be ''14.25.''")
    
    c2.write("Months in new card's 0% interest period")
    months = c2.number_input(" ", min_value = 0)
    
    
    button = st.form_submit_button(":green[**Calculate**]")
    
    
    
    
if button:
    st.write("If you moved your debt to the balance transfer card and paid it off within the 0% intro period, your only cost would be your balance transfer fee: ")
    st.markdown(f"**${round(debt * int(fee[0]) / 100)}**")
    
    st.write("If you kept your debt on your current card and paid it off in equal installments over the same period, your total interest payments would be roughly: ")
    st.markdown(f"**${round(debt * (int(apr) / 100) / 12 * months)}**")
    
    st.write("Your savings with a balance transfer")
    st.markdown("f{}")
    
    st.write("Interest calculations are estimates. Actual finance charges will vary according to your payments and your credit card's terms")
