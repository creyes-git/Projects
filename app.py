import requests
import pandas as pd
import streamlit as st

url = "https://anime-db.p.rapidapi.com/anime"
headers = {"X-RapidAPI-Key": "8af8022ddcmsh06e9119b8cc13f3p1a0e1fjsn8138c83b2c3b",
            "X-RapidAPI-Host": "anime-db.p.rapidapi.com"}

list_genders = ["Fantasy", "Drama", "Action", "Award Winning", "Slice of Life", "Suspense", "Horror", "Ecchi", "Avant Garde", "Erotica"
                "Comedy", "Hentai", "Boys Love", "Gourmet", "Girls Love", "Romance", "Adventure", "Mystery", "Supernatural", "Sci-Fi"]


querystring = {"page":"1","size":"1000","genres": "Action","sortBy":"ranking","sortOrder":"asc"}

response = requests.get(url, headers=headers, params=querystring)

df = pd.DataFrame(response.json()["data"])

# Streamlit APP:
st.title("Your Anime Explorer")
st.text("Streamlit")
st.balloons()
st.button("Click me!")
st.button('Hit me')
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')
