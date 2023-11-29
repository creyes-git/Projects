import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Naruverse", page_icon="🍥")

st.title("Chakra System")
st.image(Image.open("Naruto_app/images/naru.png"), use_column_width= True, clamp=True)
st.header("Origin:")
st.markdown("On Earth, humans didn't have chakra until Hamura and Hagoromo Ōtsutsuki were born with it, which was a result of their mother Kaguya eating their planet's chakra fruit from the God Tree. Hagoromo spread chakra to others through a practice called ninshū, intending to create peace by using the chakra to connect people's spiritual energy so that they would understand one another without even talking. However, the people did not use chakra in the way Hagoromo hoped, instead using it to connect their inner spiritual and physical energies. They kneaded their inner chakra to amplify and weaponise it, creating what is now known as ninjutsu.")
st.header("How works:")
st.markdown("Chakra is essential to even the most basic jutsu. Through various methods, the most common of which is hand seals, chakra can be controlled and manipulated to create an effect that would not be possible otherwise, such as walking on water, exhaling fire, or creating illusions. Chakra is ordinarily not visible to the unaided eye unless it is highly concentrated or manifested in large amounts.")

