import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import requests
import PIL

url = "https://narutodb.xyz/api/character?page=1&limit=1431"

response = requests.get(url).json()

df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)

st.sidebar.title("Naruto Universe")

