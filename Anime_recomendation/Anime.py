import requests
import pandas as pd
import streamlit as st
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Anime Explorer", page_icon="✨", layout="centered", initial_sidebar_state="expanded")

# API:
url = "https://anime-db.p.rapidapi.com/anime"
headers = {"X-RapidAPI-Key": "8af8022ddcmsh06e9119b8cc13f3p1a0e1fjsn8138c83b2c3b",
            "X-RapidAPI-Host": "anime-db.p.rapidapi.com"}
query = {"page": "1", "size": "10000"}

list_genders = ["Fantasy", "Drama", "Action", "Award Winning", "Slice of Life", "Suspense", "Horror", "Ecchi", "Avant Garde", "Erotica"
                "Comedy", "Hentai", "Boys Love", "Gourmet", "Girls Love", "Romance", "Adventure", "Mystery", "Supernatural", "Sci-Fi"]


st.title(":orange[**Welcome to the Anime Explorer**]")
st.image(Image.open("kimetsu.jpg"), caption="Fill your preferences and get anime recommendations")
st.write("---")

# Form
with st.form(key="search_form", clear_on_submit= True):
    type = st.radio(" Movie or TV Serie?: ", ("Movie", "TV"), index=None)
    if type == "Movie":
        a = True
    else:
        a = False
    genders = st.selectbox('Select the gender that you want to see: ', list_genders, index = None)
    status = st.radio(" Status: ", ("Finished Airing", "Not yet aired"), index = None, disabled = a)
    episodes = st.selectbox("How many episodes do you want to see: ", options= ["1-20", "21-50", "51-100", "100+"],disabled= a, index = None)
    
    button = st.form_submit_button(":orange[**Search**]")   


if button:    
    #Calling API and converting to DataFrame:
    response = requests.get(url, headers=headers, params=query)
    df = pd.DataFrame(response.json()["data"])

    df = df[df["type"] == type]
    df = df[df["status"] == status]
    df = df[df["genres"].apply(lambda x: genders in x)]    
    
    if type == "TV":
        df = df[df["episodes"] <= int(str(episodes).split("-")[1])] 
        df = df[df["episodes"] >= int(str(episodes).split("-")[0])]
    
    df = df.sort_values(by="ranking", ascending=True).head(5)
        
    for i,y, z in zip(df["image"], df["title"], df["synopsis"]):
        
        response = requests.get(i)
        
        image_data = response.content

        st.header(y)
        st.image(Image.open(BytesIO(image_data)))
        st.text(z)
        
        st.text("                                                                                                                              ")
        st.text("                                                                                                                              ")
        st.text("                                                                                                                              ")

        
    st.balloons()
