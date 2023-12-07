import pandas as pd
import requests
import json
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Cinema", page_icon="🎥",layout= "wide")

st.sidebar.title("I'm your movie partner")

c1,c2,c3,c4 = st.columns(4)
c1.title(f"Trending today:")
c2.image(Image.open("Cinema/images/1.png"))
