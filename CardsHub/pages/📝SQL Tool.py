import pandas as pd
import sqlite3 as sql
import streamlit as st 
import streamlit_lottie as st_lottie
import json

connection = sql.connect("Cards.db")
cursor = connection.cursor()

# functions:
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def sql_interpreter(sql_code: str):
    try:
        cursor.execute(sql_code)
        df = pd.DataFrame(cursor.fetchall())
        return df
    except:
        return st.error("You have an error in your SQL syntax; check your query and try again.")
    
    
c1, c2,c3 = st.columns(3)
with c2:
    st_lottie(load_lottiefile("images/SQL.json"), height = 111, quality = "high")

with c2:
    st.title(":rainbow[**SQL Interpreter**]")
    sql_code = st.text_area("Enter your SQL code here")
    run = st.button(":rainbow[**Run Query**]")

    