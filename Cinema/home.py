import pandas as pd
import requests
import json
import streamlit as st
from PIL import Image
import emoji

st.set_page_config(page_title="Cinema", page_icon="🎬",layout= "wide")

st.title(f"I'm your movie recomendator 🤖")
c1,c2,c3,c4,c5 = st.columns(5)
c1.header(f"Trending today:")
c2.image(Image.open("Cinema/images/1.png"))
