import pandas as pd
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Naruverse", page_icon="🍥")

url = "https://narutodb.xyz/api/character?page=1&limit=1431"
response = requests.get(url).json()

df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)
df.dropna(axis=0, subset=["debut","natureType","jutsu"], inplace=True)

st.title("Naruto Characters")
st.image(Image.open("Naruto_app/images/characters.jpg"), use_column_width= True, clamp=True)
st.warning("Choose the character you want to know more about")

# selectbox
character = st.selectbox(label="Character", options= df["name"].unique())
#character picked
picked = df[df["name"] == character]

st.markdown(" ")
st.markdown(" ")

c1, c2, c3 = st.columns(3)

# column 1
c1.markdown(picked["name"].values[0])

response = requests.get(picked["images"].values[0][0])
response_bytes = BytesIO(response.content)
c1.image(Image.open(response_bytes),clamp=True,width=150)

# column 3
elements = ["Fire Release", "Wind Release", "Lightning Release", "Earth Release",
"Water Release", "Yin Release", "Yang Release","Yin-Yang Release"]

for i in picked["natureType"]:
    if i in elements:
        c3.image(Image.open(f"Naruto_app/images/Yang Release.png"),clamp=True,width=50)
