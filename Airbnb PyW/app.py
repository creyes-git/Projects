import polars as pl
import pygwalker as pyg
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Airbnb Dashboard", page_icon=":house:", layout="wide", initial_sidebar_state="collapsed")

df = pd.read_csv("Airbnb_Data.csv")
st.dataframe(df)