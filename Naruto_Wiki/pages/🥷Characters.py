import pandas as pd
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Naruto Wiki", page_icon="🍥")

url = "https://narutodb.xyz/api/character?page=1&limit=1431"
response = requests.get(url).json()

df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)
df.dropna(axis=0, subset=["debut","natureType","jutsu"], inplace=True)
df.drop(index=df.index[0], inplace=True)

st.warning("Choose the character you want to know more about")
st.title("Naruto Characters")
st.image(Image.open("/workspaces/Projects/Naruto_Wiki/images/characters.jpg"), use_column_width= True, clamp=True)

# selectbox
character = st.selectbox(label="Character", options= df["name"].unique())
#character picked
picked = df[df["name"] == character]

st.markdown(" ")
st.markdown(" ")

c1, c2, c3, c4 = st.columns(4)

# column 1
# name
c1.markdown(picked["name"].values[0]+": ")
# profile picture
try:
    response = requests.get(picked["images"].values[0][0])
    response_bytes = BytesIO(response.content)
    c1.image(Image.open(response_bytes),clamp=True,width=150)
except:
    c1.warning("No Profile Picture")

# rank
rank = str(picked["rank"].values[0])

if "Kage" in rank:
    c1.markdown("Rank: Kage")
    
elif "Jōnin" in rank:
    c1.markdown("Rank: Jōnin")
    
elif "Chūnin" in rank:
    c1.markdown("Rank: Chūnin")

elif "Genin" in rank:
    c1.markdown("Rank: Genin")

else:
    c1.markdown("Rank: None")
    
# tools
c1.subheader("Tools: ")
try:
    for i in picked["tools"].values[0]:
        c1.markdown(i)
except:
    c1.warning("No Tools")
    
# column 4
elements = ["Fire Release", "Wind Release", "Lightning Release", "Earth Release",
"Water Release", "Yin Release", "Yang Release","Yin-Yang Release"]

c4.markdown("Element Nature: ")
try:
    for i in picked["natureType"].values[0]:
        if i in elements:
            c4.image(Image.open(f"/workspaces/Projects/Naruto_Wiki/images/{i}.png"),clamp=True,width=100)
        else:
            c4.warning("No Element")
            break
except:
    c4.warning("No Element")
    

# column 3
c3.markdown("Jutsu List:")
count = 0
for i in picked["jutsu"].values[0]:
    if "<" not in i and ">" not in i and "[" not in i and "]" not in i and "(" not in i and ")" not in i and "{" not in i and "}" not in i:
        c3.markdown(i)
        count += 1
    else: 
        if count == 0:
            c3.warning("No Jutsu Available")
        break
    
# column 2
c2.markdown("Debut: ")
debut = str(str(picked["debut"].values[0]).split(",")[0]).split(":")[1]
debut = debut.replace("'","")
c2.markdown("Manga: "+ debut.split("o")[1])

def mayus(string):
    for i in string.capitalize():
        if i == " ":
            string[i+1].upper()
    return string    

c2.header("Family: ")
family = str(str(picked["family"].values[0]).replace("{","")).replace("}","")
lista = list(family.split(","))
for i in lista:
    i = str(i).replace("'","")
    i = i.title()
    c2.markdown(i)
