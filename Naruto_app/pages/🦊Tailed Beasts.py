import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Naruverse", page_icon="🍥")

st.image(Image.open("Naruto_app/images/all beasts.png"), use_column_width= True)

st.image(Image.open("Naruto_app/images/1 cola.png"), use_column_width= 50, caption= "Shukaku")
