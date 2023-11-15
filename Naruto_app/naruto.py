import pandas as pd
import numpy as np
import streamlit as st
import requests
from PIL import Image

url = "https://narutodb.xyz/api/character?page=1&limit=1431"

response = requests.get(url).json()

df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)

#Sidebar:
st.sidebar.image(Image.open("Naruto_app/images.jpg"), width=200)
st.sidebar.title("Naruto Universe")
st.sidebar.markdown("##")