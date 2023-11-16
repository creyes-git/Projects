import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import requests
from PIL import Image


url = "https://narutodb.xyz/api/character?page=1&limit=1431"

#Dataframe:
response = requests.get(url).json()
df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)


#Sidebar:
st.sidebar.image(Image.open("Naruto_app/icons8-naruto-512.png"), width=00, clamp=True, caption= "Naruverse App")
characters = st.button("🍥Characters")
villages = st.button("🏛️Villages")
clans = st.button("🥷🏻Clans")
tailed_beasts = st.button("🦊Tailed Beasts")
akatsuki = st.button("🩸Akatsuki")
