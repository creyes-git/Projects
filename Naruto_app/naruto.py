import pandas as pd
import numpy as np
import streamlit as st
import requests
from PIL import Image


url = "https://narutodb.xyz/api/character?page=1&limit=1431"

#Dataframe:
response = requests.get(url).json()
df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)


#Sidebar:
st.sidebar.image(Image.open("Naruto_app/icons8-naruto-512.png"), width=90, clamp=True, caption= "Naruverse App")
st.sidebar.text("__________________________________________________________________________________________________--")
introduction = st.sidebar.button("📖Introduction")
characters = st.sidebar.button("🍥Characters")
villages = st.sidebar.button("🏛️Villages")
clans = st.sidebar.button("🥷🏻Clans")
tailed_beasts = st.sidebar.button("🦊Tailed Beasts")
akatsuki = st.sidebar.button("🩸Akatsuki")
