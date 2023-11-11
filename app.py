import requests
import pandas as pd
import streamlit as st
from PIL import Image

url = "https://anime-db.p.rapidapi.com/anime"
headers = {"X-RapidAPI-Key": "8af8022ddcmsh06e9119b8cc13f3p1a0e1fjsn8138c83b2c3b",
            "X-RapidAPI-Host": "anime-db.p.rapidapi.com"}

list_genders = ["Fantasy", "Drama", "Action", "Award Winning", "Slice of Life", "Suspense", "Horror", "Ecchi", "Avant Garde", "Erotica"
                "Comedy", "Hentai", "Boys Love", "Gourmet", "Girls Love", "Romance", "Adventure", "Mystery", "Supernatural", "Sci-Fi"]


querystring = {"page":"1","size":"1000","genres": "Action","sortBy":"ranking","sortOrder":"asc"}

response = requests.get(url, headers=headers, params=querystring)

df = pd.DataFrame(response.json()["data"])

# Streamlit APP:________________________________________________________________________________________________________________________
picture = Image.open("kimetsu.jpg")
st.image(picture, caption="WELCOME TO ANIME EXPLORER :)")

st.title("Fill your app preferences")

st.text("                                                                                                                              ")
st.text("                                                                                                                              ")
st.text("                                                                                                                              ")

type = st.radio(" Movie or TV Serie?: ", ("Movie", "Serie"), index=0)

genders = st.multiselect('Select the gender that you want to see: ', list_genders, default=list_genders[0])

episodes = st.selectbox("How many episodes do you want to see: ", options= ["1-50", "51-100", "100-200", "200+"], index=0)

status = st.radio(" Status: ", ("Finished Airing", "Not yet aired"), index=0)


#search details:
querystring = {"page":"1","size":"10000", "sortBy":"ranking","sortOrder":"asc"}

response = requests.get(url, headers=headers, params=querystring)

df = pd.DataFrame(response.json()["data"])
df = df.query("type == @type")
df = df.query("status == @status")
df = df.query("episodes == @episodes")
df = df.query("genres in @genders")

st.dataframe(df)
