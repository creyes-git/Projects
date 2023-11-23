import pandas as pd
import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Naruverse", page_icon="🍥")

st.title("Naruto Universe Characters")
st.image(Image.open("Naruto_app/images/characters.png"), use_column_width= True, clamp=True)

url = "https://narutodb.xyz/api/character?page=1&limit=1431"

response = requests.get(url).json()

df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)




character = st.selectbox("Chose the character", df["name"].unique())

def show_character(character):
    df = df[df["name"] == character]
    
    return st.write(df)

show_character(character)
