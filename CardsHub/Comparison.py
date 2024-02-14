import pandas as pd
import sqlite3 as sql
import streamlit as st

st.set_page_config(page_icon= "💳",page_title= "CardsHwub", layout= "wide", initial_sidebar_state= "expanded")

connection = sql.connect("Cards.db")
cursor = connection.cursor()