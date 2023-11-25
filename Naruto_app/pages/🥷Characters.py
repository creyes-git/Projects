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
df.drop(index=df.index[0], inplace=True)

st.warning("Choose the character you want to know more about")
st.title("Naruto Characters")
st.image(Image.open("Naruto_app/images/characters.jpg"), use_column_width= True, clamp=True)

# selectbox
character = st.selectbox(label="Character", options= df["name"].unique())
#character picked
picked = df[df["name"] == character]

st.markdown(" ")
st.markdown(" ")

c1, c2, c3, c4 = st.columns(4)

# column 1
c1.markdown(picked["name"].values[0]+": ")

response = requests.get(picked["images"].values[0][0])
response_bytes = BytesIO(response.content)
c1.image(Image.open(response_bytes),clamp=True,width=150)

for i in picked["rank"].values[0]:
    c1.markdown(i)

# column 4
elements = ["Fire Release", "Wind Release", "Lightning Release", "Earth Release",
"Water Release", "Yin Release", "Yang Release","Yin-Yang Release"]

c4.markdown("Element Nature: ")
try:
    for i in picked["natureType"].values[0]:
        if i in elements:
            c4.image(Image.open(f"Naruto_app/images/{i}.png"),clamp=True,width=100)

except:
    c4.warning("No Element")
    

# column 3
c3.markdown("Jutsu List:")
for i in picked["jutsu"].values[0]:
    c3.markdown(i)

# column 2
c2.markdown("Debut: ")
for i in picked["debut"].values[0]:
    c2.markdown(i)



c2.markdown(picked["tools"].values[0])
c2.markdown(picked["family"].values[0])

c1.markdown(picked["personal"].values[0])
