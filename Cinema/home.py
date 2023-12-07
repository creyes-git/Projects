import pandas as pd
import requests
import json
import streamlit as st
from PIL import Image
from my_module import icon_calendar as icon

st.set_page_config(page_title="Cinema", page_icon="🎬",layout= "wide")

url = "https://api.themoviedb.org/3/trending/movie/week?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MjJlNDk5MTgxN2NmZDFjODM4MWU0ZTMzMGNhYWE1NiIsInN1YiI6IjY1NzExMTg4ZTRjOWViMDBmZGUwNWYwOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7nxsSCK52vWr4esGTNBgCG04SwJKbrHdNNUe2ieP-hI"
}

response = requests.get(url, headers=headers)
df = pd.DataFrame(response.json()["results"])

st.sidebar.title("I'm your movie partner")

i = st.image(Image.open("Cinema/pages/1.png"))
st.title(f"Trending today: {i}")
