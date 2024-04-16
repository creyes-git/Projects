import pandas as pd
import sqlite3 as sql
import streamlit as st

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

st.title(":red[**Utilization**] :green[**Calculator**]")

with st.form(key="utilization_form", clear_on_submit= True):
    c1, c2, c3 = st.columns(3)
    n = 1
    
    with st.container():
        c1.number_input("Card Balance",key = "1", min_value = 0, step = 100, help = "This is how much debt you currently have on your card")
        c3.number_input("Card Limit",key = "1.5", min_value = 0, step = 100, help = "This is your credit card's maximum limit")
            
    
        
        
    button = st.form_submit_button(label="Calculate")