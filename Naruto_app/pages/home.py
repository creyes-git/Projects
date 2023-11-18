import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Naruverse", page_icon="🍥", layout="wide")

#Introduction
c1, c2 , c3, c4, c5 = st.columns(5)
c1.image(Image.open("images\\wp2725528-naruto-kakashi-wallpaper.png"), width=150, clamp=True)
c2.image(Image.open("images\\wp10367350-minato-minimalist-wallpapers.jpg"), width=150, clamp=True)
c3.image(Image.open("images\\Landing Page.png"), width=150, clamp=True)
c4.image(Image.open("images\\wp10926937-minimalist-4k-naruto-wallpapers.png"), width=150, clamp=True)
c5.image(Image.open("images\\wp5129198-anime-lambang-uciha-wallpapers.jpg"), width=150, clamp=True)
st.title("About Naruto")
st.text('''NARUTO is a manga series created by MasashiKishimoto 
that was serialized in Weekly ShonenJump. Met with popularity 
followingits initial publication in 1999, the series went on to receive 
an anime adaptation that commenced broadcasting in 2002. The manga 
concluded in 2014 with a total of 700 chapters. The total number of print 
copies sold globally exceeds 250 million, and even now NARUTO events, 
games, merchandise,and more continue to be created and released for fans 
to enjoy a testament to the series’ 
enduring influence and popularityaround the world.''')                


'''#Sidebar:
st.sidebar.image(Image.open("images\\icons8-naruto-512.png"), width=90, clamp=True, caption= "Naruverse")
introduction = st.sidebar.button("📖Introduction")
tailed_beasts = st.sidebar.button("🦊Tailed Beasts")
characters = st.sidebar.button("🍥Characters")
akatsuki = st.sidebar.button("🩸Akatsuki")
villages = st.sidebar.button("🏛️Villages")
clans = st.sidebar.button("🥷🏻Clans")'''
