import streamlit as st
import pandas as pd
import sqlite3 as sql
import json
import streamlit

st.set_page_config(page_icon= "",page_title= "CreditHub", layout= "wide")

connection = sql.connect("CreditHub\\DB\\Database.db")
cursor = connection.cursor()