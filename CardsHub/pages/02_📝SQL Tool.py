import pandas as pd
import sqlite3 as sql
import streamlit as st 

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "centered", initial_sidebar_state= "expanded")

connection = sql.connect("Cards.db")
cursor = connection.cursor()

st.title(":rainbow[**SQL Interpreter**]🗄️")

with st.form(key="sql_query_form", clear_on_submit= True):
    query = st.text_area("Enter your SQL code here").strip()
    
    with st.expander("Check the Table Info before querying"):
        st.warning(f":rainbow[**Table Name: Cards**]")
        try:
            df = pd.DataFrame(cursor.execute("SELECT * FROM cards"), columns=[i[0] for i in cursor.description])
            st.dataframe(df)
        except:
            st.error("Table not found")
    
    run = st.form_submit_button(":rainbow[**Run Query**]")
    
if run and query.upper().startswith("SELECT"):
    try:
        st.dataframe(pd.DataFrame(cursor.execute(query), columns=[i[0] for i in cursor.description]))
        
        connection.commit()
        
    except:
        st.error("You have an error in your SQL syntax; check your query and try again.")

else:
    st.warning("Please enter a valid SQL query, you can execute SELECT queries only.")
    
    connection.close()
  


