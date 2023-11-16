import pandas as pd
import numpy as np
#import plotly.express as px
import streamlit as st
import requests
from PIL import Image


url = "https://narutodb.xyz/api/character?page=1&limit=1431"

#Dataframe:
response = requests.get(url).json()
df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)


#Introduction:
def landing_page():
    st.image(Image.open("Naruto_app/Landing Page.png"), use_column_width= True)
    st.title("About Naruto")
    st.text('''NARUTO is a manga series created by MasashiKishimoto 
that was serialized in Weekly ShonenJump. Met with popularity 
followingits initial publication in 1999, the series went on to receive 
an anime adaptation that commenced broadcasting in 2002. The manga 
concluded in 2014 with a total of 700 chapters. The total number of print 
copies sold globally exceeds 250 million, and even now NARUTO events, 
games, merchandise,and more continue to be created and released for fans 
to enjoy a testament to the series’ enduring influence and 
popularityaround the world.''')      
    
landing_page()


#Sidebar:
st.sidebar.image(Image.open("Naruto_app/icons8-naruto-512.png"), width=90, clamp=True, caption= "Naruverse App")
st.sidebar.text("__________________________________________________________________________________________________--")
introduction = st.sidebar.button("📖Introduction")
characters = st.sidebar.button("🍥Characters")
villages = st.sidebar.button("🏛️Villages")
clans = st.sidebar.button("🥷🏻Clans")
tailed_beasts = st.sidebar.button("🦊Tailed Beasts")
akatsuki = st.sidebar.button("🩸Akatsuki")

if introduction:
    landing_page()
    
if characters:
    st.dataframe(df)
