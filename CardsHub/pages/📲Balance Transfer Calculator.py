import sqlite3 as sql
import streamlit as st
import pandas as pd
import json

connection = sql.connect("Cards.db")
cursor = connection.cursor()

st.title(":red[Balance tran]:green[sfer calculator]")

with st.form(key="balance_transfer_form", clear_on_submit= True):
    st.warning("Transferring debt to a credit card with a 0% introductory annual percentage rate, or APR, could save you hundreds of dollars in interest while you pay down your debt.")
    c1, c2 = st.columns(2)
    
    c1.write("Credit card debt you want to transfer to the new card (in dollars)")
    debt =c1.number_input(" ")
    
    c2.write("Interest rate (APR) charged on that current debt")
    apr = c2.number_input(":")
    
    button = st.form_submit_button(":green[**Calculate**]")