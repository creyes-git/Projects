import streamlit as st
from PIL import Image

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded", theme = "light")

c1, c2 = st.columns(2)
c1.image(Image.open("images/home.png"), width= 225)
c2.title(":green[**Welcome To**]")
c2.title(":red[**CardHub!**]")

st.title("App Pages Content: ")
with st.container():
    st.write("- :red[**Add Card**]: Add a new card with all the information to the app database")
    st.write("- :green[**Comparison Tool**]: Choose two cards to compare their features")
    st.write("- :red[**SQL Tool**]: This is a SQL tool to run Queries on the database")
    st.write("- :green[**Credit Building**]: Get a full guide, tips and tricks on how to build a credit card wisely")
    st.write("- :red[**Popular Strategies**]: Check the most popular credit card strategies for individuals and families") 
    st.write("- :red[**Credit Market**]: See real time data about the credit market, from banks and credit cards") 


# Info and sources
with st.expander(":rainbow[**About this app and who made it**]"):
    with st.container():
        st.write("- :red[**Data Source**]: [Bankrate](https://www.bankrate.com/)")
        st.write("- :blue[**Info**]: The data is collected from Bankrate.com and will be updated every month")
        st.write("- :green[**Source Code**]: [GitHub](https://github.com/carlosreyes98/Projects/tree/main/CardsHub)")
        st.write("- :orange[**Made by**]: **Carlos Reyes**")
            