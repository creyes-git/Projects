import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title="World Building", page_icon="🍥")

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

st.image(Image.open("Naruto_app//images//Land_of_Earth_Symbol.png"),caption="The Land of Earth", width=100)
st.markdown("The Land of Earth (土の国, Tsuchi no Kuni) has seen little attention in the series thus far. It is located north-west of the Land of Fire. Its government leader is the Earth Daimyō. The country is mostly comprised of desolate, rocky areas. The border of the Land of Earth runs along a rocky mountain range, blocking communication with other countries. The wind blowing from the north passes over these mountains, carrying small rocks from the Land of Earth to the surrounding countries. This famous natural phenomenon is called Rock Rain (岩雨, Gan'u).")

st.image(Image.open("Naruto_app//images//Land_of_Fire_Symbol.png"),caption="The Land of Fire", width=100)
st.markdown("The Land of Fire (火の国, Hi no Kuni) is one of the largest and most powerful countries seen, and is the home of the main characters of the series. Its government leader is the Fire Daimyō. The Land of Fire was the first country to adopt a ninja village, Konohagakure, a custom other countries would soon adopt. The Land of Fire is appropriately oriented towards the element of fire, typically having very bright and warm weather. While not the physically largest country, it has the largest hidden village.")

st.image(Image.open("Naruto_app//images//Land_of_Iron_Symbol.png"),caption="The Land of Iron", width=100)
st.markdown("The Land of Iron (鉄の国, Tetsu no Kuni) is an icy, snow-covered country located among three mountains called the Three Wolves (三狼, Sanrō). Unlike other countries of the world whose militaries use shinobi, the Land of Iron's military is made up of samurai. Due to the differing ideologies between shinobi and samurai – as well as the fact that the Land of Iron's samurai are quite formidable – there is an agreement among shinobi not to interfere with the Land of Iron.")

st.image(Image.open("Naruto_app//images//Land_of_Lightning_Symbol.png"),caption="The Land of Lightning", width=100)
st.markdown("The Land of Lightning (雷の国, Kaminari no Kuni) is located on a peninsula north-east of the Land of Fire and is one of the Five Great Shinobi Countries. Its government leader is the Lightning Daimyō. In the centre of the country are vast mountain ranges, whose many thunderstorms are said to give the country its name. From these mountain ranges, many rivers flow to the sea, creating a very crooked coastline that displays an impressive oceanic beauty. There are many hot springs located within the country. The country's western border with the Land of Frost has a large desert.")

st.image(Image.open("Naruto_app//images//Land_of_Snow_Symbol.png"),caption="The Land of Snow", width=100)
st.markdown("The Land of Snow (雪の国, Yuki no Kuni) is a nation introduced in Naruto the Movie: Ninja Clash in the Land of Snow, that is also briefly mentioned in the anime and in the Hiden novels. The nation would eventually be introduced in the manga.Originally, the country was a small, but peaceful place. However, it was taken over by a tyrant, Dotō Kazahana, after he and his mercenaries killed his older brother and predecessor, Sōsetsu Kazahana.")

st.image(Image.open("Naruto_app//images//Land_of_Sound_Symbol.png"),caption="The Land of Sound", width=100)
st.markdown("The Land of Sound (音の国, Oto no Kuni) is a neighbouring country of the Land of Fire. It is a relatively new country in the political scene, though it has existed for some time under the name of the Land of Rice Fields (田の国, Ta no Kuni, English TV: Land of Rice Paddies). According to the anime, Orochimaru conquered the country and convinced its daimyō to let him establish his own ninja village.")

st.image(Image.open("Naruto_app//images//Land_of_Water_Symbol.png"),caption="The Land of Water", width=100)
st.markdown("The Land of Water (水の国, Mizu no Kuni) also known as the Land of Mist (霧の国, Kiri no Kuni).[9][10] It is composed of many islands, with each having its own unique traditions. The country's weather is typically cool and the islands are usually covered by mist. The islands themselves also feature many lakes. In some places, like the area where Haku grew up, it is very cold and snows quite a bit. The nation is oriented towards the element of water. Its government leader is the Water Daimyō.")

st.image(Image.open("Naruto_app//images//Land_of_Wind_Symbol.png"),caption="The Land of Wind", width=100)
st.markdown("The Land of Wind (風の国, Kaze no Kuni) is one of the more prominent countries in the series. It is located to the south-west of the Land of Fire and borders the Land of Rivers and Amegakure. Its government leader is the Wind Daimyō. The country covers a vast realm, but is significantly composed of deserts and thus has little productivity.[11] Because there is very little rainfall throughout the year, the people of the country live in villages built on one of the desert's many oases. Despite the country's extremely harsh environment, it has a large population. Although they have warred with each other in the past, the Land of Wind is now on good terms with the Land of Fire, with a great deal of trade going on between the two countries.")


st.image(Image.open("Naruto_app//images//kages.png"), use_column_width= True, clamp=True)

st.title("Hidden Villages")
st.markdown("Hidden Villages are parts of countries in which the country's ninja reside. Their heads stand equally with the landlords ruling the countries they are a part of. A Hidden Village maintains its economy by training its citizens to be ninja from a young age and using them as manpower in various missions others would be willing to pay for, from weeding a garden for a single payment to receiving a constant budget from the country it resides in for being soldiers in case the country is involved in a war.")

st.image(Image.open("Naruto_app//images//Konohagakure_Symbol.png"),caption="Konohagakure", width=100)
st.markdown("Konohagakure (木ノ葉隠れの里, Konohagakure no Sato, English TV: Village Hidden in the Leaves or Hidden Leaf Village, literally meaning: Village Hidden by Tree Leaves) is the hidden village of the Land of Fire. As the village of one of the Five Great Shinobi Countries, Konohagakure has a Kage as its leader known as the Hokage, of which there have been eight in its history. Konoha resides deep within a forest at the base of a mountain known as the Hokage Rock, which has the faces of all those who have taken the office of Hokage engraved on it.")

st.image(Image.open("Naruto_app//images//Kirigakure_Symbol.png"),caption="Kirigakure", width=100)
st.markdown("Kirigakure (霧隠れの里, Kirigakure no Sato, English TV: Village Hidden in the Mist, literally meaning: Village Hidden by Mist) is the hidden village of the Land of Water. As the village of one of the Five Great Shinobi Countries, Kiri has a Kage as its leader known as the Mizukage, of which there have been six in its history. Befitting its name, the village is surrounded by a thick mist, with several mountains in the background, making it difficult to find by foreigners.")

st.image(Image.open("Naruto_app//images//Kumogakure_Symbol.png"),caption="Kumogakure", width=100)
st.markdown("Kumogakure (雲隠れの里, Kumogakure no Sato, English TV: Hidden Cloud Village, literally meaning: Village Hidden by Clouds) is the hidden village of the Land of Lightning and was founded by the First Raikage. As the village of one of the Five Great Shinobi Countries, Kumogakure has a Kage as its leader known as the Raikage, of which there have been five in its history. The village is located in a range of tall mountains, and is literally hidden in the clouds.")

st.image(Image.open("Naruto_app//images//Iwagakure_Symbol.png"),caption="Iwagakure", width=100)
st.markdown("Iwagakure (岩隠れの里, Iwagakure no Sato, English TV: Hidden Stone Village, literally meaning: Village Hidden by Rocks) is the hidden village of the Land of Earth. As the village of one of the Five Great Shinobi Countries, Iwagakure has a Kage as its leader known as the Tsuchikage, of which there have been four in its history. The rocky mountain ranges that surround the village provide a natural stronghold that it is very proud of.")

st.image(Image.open("Naruto_app//images//Sunagakure_Symbol.png"),caption="Sunagakure", width=100)
st.markdown("Sunagakure (砂隠れの里, Sunagakure no Sato, literally meaning: Village Hidden by Sand) is the hidden village of the Land of Wind. As the village of one of the Five Great Shinobi Countries, Sunagakure has a Kage as its leader known as the Kazekage, of which there have been five in its history. Being surrounded by desert offers the village a natural deterrent against invasion, as few foreign powers would be willing to endure the sandstorms and water scarcity common to Suna.")


