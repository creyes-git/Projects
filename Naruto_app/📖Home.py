import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Naruverse", page_icon="🍥")

#Introduction
c1, c2 , c3, c4, c5 = st.columns(5)
c1.image(Image.open("Naruto_app/images/wp2725528-naruto-kakashi-wallpaper.png"), width=150, clamp=True)
c2.image(Image.open("Naruto_app/images/wp10367350-minato-minimalist-wallpapers.jpg"), width=150, clamp=True)
c3.image(Image.open("Naruto_app/images/Landing Page.png"), width=150, clamp=True)
c4.image(Image.open("Naruto_app/images/wp10926937-minimalist-4k-naruto-wallpapers.png"), width=150, clamp=True)
c5.image(Image.open("Naruto_app/images/wp5129198-anime-lambang-uciha-wallpapers.jpg"), width=150, clamp=True)

st.title("About Naruto")
st.markdown('''NARUTO is a manga series created by Masashi Kishimoto that was serialized in Weekly ShonenJump. 
Met with popularity followingits initial publication in 1999, the series went on to receive an anime adaptation
that commenced broadcasting in 2002. The manga concluded in 2014 with a total of 700 chapters. The total number 
of print copies sold globally exceeds 250 million, and even now NARUTO events, games, merchandise,and more 
continue to be created and released for fans to enjoy a testament to the series’ enduring influence and popularityaround the world.''')                

st.title("Synopsis")
st.markdown('''Twelve years before the start of the series, the ninja village of Konohagakure was attacked by the Nine-Tailed Demon Fox.
The village was only saved from complete destruction by the actions of Konoha's leader, the Fourth Hokage, who sacrificed his life to 
seal the Nine-Tails into a newborn: Naruto Uzumaki. Orphaned by the attack, Naruto grew up shunned by most of the villagers, who hated 
and feared him because of the Nine-Tails trapped within him. Unaware of the monster he contained, Naruto longed for acknowledgment, 
and so vowed to one day become the greatest Hokage the village had ever seen.''')

st.title("Details of Naruto MANGA")
st.markdown("- Copies in circulation: 250 million copies in 47 countries and regions")
st.markdown("- Tankōbon: 72 tankōbon released in Japan")
st.markdown("- Volumes: 72 volumes")
st.markdown("- Naruto is one of the best-selling manga series in history. In Japan, there are 153 million copies in circulation, and 97 million copies elsewhere.") 
st.markdown("- Naruto is also a popular anime series. On the MyAnimeList website, Naruto is ranked 7th, behind newer anime like My Hero Academia, One Punch Man, and Attack on Titan.")

df = pd.read_csv("Naruto_app/data_anime.csv")
chart_1 = st.bar_chart(df)
