import pandas as pd
import streamlit as st
from PIL import Image
from Naruto_app.pages.data import show_character
from Naruto_app.pages.data import df
st.set_page_config(page_title="Naruverse", page_icon="🍥")

st.title("Naruto Characters")
st.image(Image.open("Naruto_app/images/characters.png"), use_column_width= True, clamp=True)

character = st.selectbox("Chose the character", df["name"].unique())


