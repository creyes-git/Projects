import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Naruverse", page_icon="🍥")

st.title("Naruto World Construction")
st.markdown('''The Naruto series is set on a fictional terrestrial blue planet called Earth. Most of the series takes place on a large 
continent that is divided into a number of different countries; additional continents are occasionally depicted in supplementary media. 
This region and the society that prevails within it is often referred to as the Ninja World (忍界, Ninkai) or Shinobi World (忍の世界, Shinobi no Sekai).''')

st.title("Countries")
st.markdown('''Countries operate as separate political entities and are presumably all monarchies, ruled by daimyō who stand as a ruler 
for the entire country. Hidden Village heads are the generals that take care of shinobi matters. The Naruto world is similar to feudal 
Japan in many aspects; those countries maintain balance between themselves through nothing but power. Treaties are periodically signed, 
but they are generally not worth much more than the paper they are written on.''')
st.image(Image.open("Naruto_app//images//Naruto_World_Map.png"), use_column_width= True, clamp=True)

st.image(Image.open("Naruto_app//images//Land_of_Earth_Symbol.png"),caption="The Land of Earth")
st.markdown("The Land of Earth (土の国, Tsuchi no Kuni) has seen little attention in the series thus far. It is located north-west of the Land of Fire. Its government leader is the Earth Daimyō. The country is mostly comprised of desolate, rocky areas. The border of the Land of Earth runs along a rocky mountain range, blocking communication with other countries. The wind blowing from the north passes over these mountains, carrying small rocks from the Land of Earth to the surrounding countries. This famous natural phenomenon is called Rock Rain (岩雨, Gan'u).")
