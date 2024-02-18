import pandas as pd
import sqlite3 as sql
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json
import requests

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")


st.image(Image.open("images/home.png"))





# Info and sources
with st.expander(":rainbow[**About this app and who made it**]", expanded= True):
    with st.container():
        st.write("- :red[**Data Source**]: [Bankrate](https://www.bankrate.com/)")
        st.write("- :blue[**Info**]: The data is collected from Bankrate.com and will be updated every month")
        st.write("- :green[**Source Code**]: [GitHub](https://github.com/carlosreyes98/Projects/tree/main/CardsHub)")
        st.write("- :orange[**Made by**]: **Carlos Reyes**")
            