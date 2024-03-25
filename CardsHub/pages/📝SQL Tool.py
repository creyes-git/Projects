import pandas as pd
import sqlite3 as sql
import streamlit as st 

connection = sql.connect("Cards.db")
cursor = connection.cursor()

st.title(":rainbow[**SQL Interpreter**]🗄️")

with st.form(key="sql_query_form", clear_on_submit= True):
    sql_code = st.text_area("Enter your SQL code here")
    
    with st.expander("Check the Table Info before querying"):
        st.warning(f":rainbow[**Table Name: Cards**]")
        df = pd.DataFrame(cursor.execute("SELECT * FROM cards"), columns=[i[0] for i in cursor.description])
        st.dataframe(df)

    
    run = st.form_submit_button(":rainbow[**Run Query**]")
    x = sql_code.strip()
    
if run:  
    try:
        if x.startswith("SELECT") or x.startswith("select"):
            st.dataframe(pd.DataFrame(cursor.execute(sql_code), columns=[i[0] for i in cursor.description]))
        else:
            cursor.execute(sql_code)
            connection.commit()
    except:
        st.error("You have an error in your SQL syntax; check your query and try again.")
  


