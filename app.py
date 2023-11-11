import requests
import pandas as pd
import streamlit as st
from PIL import Image

url = "https://anime-db.p.rapidapi.com/anime"

headers = {"X-RapidAPI-Key": "8af8022ddcmsh06e9119b8cc13f3p1a0e1fjsn8138c83b2c3b",
            "X-RapidAPI-Host": "anime-db.p.rapidapi.com"}

query = {"page": "1", "size": "10000"}

list_genders = ["Fantasy", "Drama", "Action", "Award Winning", "Slice of Life", "Suspense", "Horror", "Ecchi", "Avant Garde", "Erotica"
                "Comedy", "Hentai", "Boys Love", "Gourmet", "Girls Love", "Romance", "Adventure", "Mystery", "Supernatural", "Sci-Fi"]

key = True

# Streamlit APP:
picture = Image.open("kimetsu.jpg")
st.image(picture, caption="WELCOME TO ANIME EXPLORER :)")

st.title("Fill your app preferences")

st.text("                                                                                                                              ")
st.text("                                                                                                                              ")
st.text("                                                                                                                              ")

genders = st.multiselect('Select the gender that you want to see: ', list_genders, default= None)

type = st.radio(" Movie or TV Serie?: ", ("Movie", "TV"), index=0)


if type == "TV":
    key = False

episodes = st.selectbox("How many episodes do you want to see: ", options= ["1-50", "51-100", "100-200", "200-1000"],disabled= key)

status = st.radio(" Status: ", ("Finished Airing", "Not yet aired"), index=0)


#search button:  
button = st.button("Search", type= "primary")   



if button:    
    #Calling API:
    response = requests.get(url, headers=headers, params=query)
    df = pd.DataFrame(response.json()["data"])
    
    df = df[df["type"] == type]
    
    df = df[df["status"] == status]
    
    
        
    if type == "TV":
        df = df[df["episodes"] <= int(str(episodes).split("-")[1])]
        
    st.dataframe(df)

