import streamlit as st
from PIL import Image

st.set_page_config(page_icon= "💳",page_title= "CardsHub", layout= "wide", initial_sidebar_state= "expanded")

c1, c2 = st.columns(2)
c1.image(Image.open("images/home.png"), width= 225)
c2.title(":green[**Welcome To**]")
c2.title(":red[**CardHub!**]")

st.title(":red[**Pages**] :green[**Content:**] ")
with st.container():
    st.write("- :red[**Add Card**]: Add new cards with all the information to the app database")
    st.write("- :green[**SQL Tool**]: Run Queries and explore the data")
    st.write("- :red[**Comparison Tool**]: Choose two cards to compare their features and pick well")
    st.write("- :green[**Card Match**]: Fill out the form and get recommendations for your credit card")
    st.write("- :red[**FICO vs Vantage Guide**]: Learn the basics and diferences between FICO and Vantage scores") 
    st.write("- :green[**Utilization Calculator**]: Calculate the impact of your credit utilization") 
    st.write("- :red[**Interest Calculator**]: Track your credit card's interest payments") 
    st.write("- :green[**Balance Transfer Calculator**]: Before transfer your debt, calculate the cost of your balance transfer") 


# Info and sources
with st.expander(":rainbow[**About this app and who made it**]"):
    with st.container():
        st.write("- :red[**Data Source**]: [Bankrate](https://www.bankrate.com/), [The Ascent](https://www.fool.com/the-ascent/), [The Point's Guy](https://thepointsguy.com/credit-cards/hilton/)")
        st.write("- :blue[**Info**]: The data is collected from these websites and will be updated every month")
        st.write("- :green[**Source Code**]: [GitHub](https://github.com/carlosreyes98/Projects/tree/main/CardsHub)")
        st.write("- :orange[**Made by**]: **Carlos Reyes**")
            