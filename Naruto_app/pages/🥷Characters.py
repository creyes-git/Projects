import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Naruverse", page_icon="🍥")

st.title("Naruto Characters")
st.image(Image.open("Naruto_app/images/characters.png"), use_column_width= True, clamp=True)
