import streamlit as st
from PIL import Image
import numpy as np
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import requests
from streamlit_lottie import st_lottie
import json

# page configuration
st.set_page_config(page_title = "Pokédex",page_icon= "🎴", layout = "wide")

# css file for displaying Pokemon type (fire, water etc.)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# load cssp
local_css('PokeDEX/style.css')


# load data until 847 rows due to missing images
df = pd.read_csv('PokeDEX/pokedex.csv', keep_default_na = False).iloc[:847] 


# load lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_pokeball = load_lottiefile("PokeDEX/pokeball.json")  # replace link to local lottie file
with st.sidebar:
	st_lottie(lottie_pokeball, height = 60, quality = "high")
	text = f'<span class="icon type-text">Pokédex</span>'
	st.sidebar.markdown(text, unsafe_allow_html=True)


# sidebar for searching Pokemon
pokemon_name = str(st.sidebar.selectbox('Search your Pokemon', df['name'].str.lower().unique(), index = 4))
match = df[df['name'].str.lower() == name]
id = int(match["pokedex_number"])

# use Pokemon name and id to get image path
def get_image_path(pokemon_name, id):
	if name.startswith('Mega'):
		if name.endswith(' X'):
			path = 'PokeDEX/pokemon_images/' + str(id) + '-mega-x.png'
		elif name.endswith(' Y'):
			path = 'PokeDEX/pokemon_images/' + str(id) + '-mega-y.png'
		else:
			path = 'PokeDEX/pokemon_images/' + str(id) + '-mega.png'
	elif name.endswith(' Rotom'):
		rotom_type = name.split()[0].lower()
		path = 'PokeDEX/pokemon_images/' + str(id) + '-' + rotom_type + '.png'
	elif name.endswith(' Forme') or name.endswith(' Cloak')  or name.endswith(' Form'):
		if 'Zygarde' in name: # only 1 image present for Zygarde
			path = 'PokeDEX/pokemon_images/' + str(id) + '.png'			
		else:
			type = name.split()[1].lower()
			path = 'PokeDEX/pokemon_images/' + str(id) + '-' + type + '.png'
	elif name.startswith('Primal '):
		type = name.split()[0].lower()
		path = 'PokeDEX/pokemon_images/' + str(id) + '-' + type + '.png'
	elif name.startswith('Arceus'): 
		path = 'PokeDEX/pokemon_images/' + str(id) + '-normal.png' # this is just how Arceus is named in the image file
	else:
		path = 'PokeDEX/pokemon_images/' + str(id) + '.png'
	return path
	
 
# get basic info data
def display_basic_info(match):
	name = match['name']
	id = match['pokedex_number']
	height = str(match['height_m'])
	weight = str(match['weight_kg'])
	species = ' '.join(match['species'].iloc[0].split(' ')[:-1])
	type1 = match['type_1']
	type2 = match['type_2']
	type_number = match['type_number']
	ability1 = match['ability_1']
	ability2 = match['ability_2']
	ability_hidden = match['ability_hidden']
	
	st.title(name)
	col1, col2, col3 = st.columns(3)
	
	# col1
	try:
		col1.image(Image.open(get_image_path(name, id)))	
	except:
		col1.write('Image not available.')
	
	# col2
	with col2.container():		
		col2.write('Type')
		# html code that loads the class defined in css, each Pokemon type has a different style color
		type_text = f'<span class="icon type-{type1.lower()}">{type1}</span>'
		if type_number == 2:
			type_text += f' <span class="icon type-{type2.lower()}">{type2}</span>'
		# markdown displays html code directly
		col2.markdown(type_text, unsafe_allow_html=True)
		col2.metric("Height", height + " m")
		col2.metric("Weight", weight + " kg")
	
	# col3
	with col3.container():
		col3.metric("Species", species)
		col3.write('Abilities')
		if ability1 != '':
			col3.subheader(ability1)
		if ability2 != '':
			col3.subheader(ability2)
		if ability_hidden != '':
			col3.subheader(ability_hidden + ' (Hidden)')


def display_base_stats_type_defenses(match):
	# list to gather all type weaknesses and resistances
	weakness_2_types = []
	weakness_4_types = []
	resistance_half_types = []
	resistance_quarter_types = []
	
	# dataset only shows damage (x4, x2, x0.25, x0.5) of each type towards the Pokemon
	# manually classify the damages into weaknesses and resistances list
	for i, j in match.iterrows():
		for column, value in j.iteritems():
			if column.startswith('against_'):
				type = column.split('_')[1]
				if value == 0.5:
					resistance_half_types.append(type)
				elif value == 0.25:
					resistance_quarter_types.append(type)
				elif value == 2:
					weakness_2_types.append(type)
				elif value == 4:
					weakness_4_types.append(type)
					
	with st.container():	
		col1, col2 = st.columns(2)	
		
		# left column col1 displays horizontal bar chart of base stats
		col1.subheader('Base Stats')
		# get base stats of Pokemon and rename columns nicely
		df_stats = match[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
		df_stats = df_stats.rename(columns={'hp': 'HP', 'attack': 'Attack', 'defense': 'Defense', 'sp_attack': 'Special Attack', 'sp_defense': 'Special Defense', 'speed': 'Speed'}).T
		df_stats.columns=['stats']
		
		# plot horizontal bar chart using matplotlib.pyplot
		fig, ax = plt.subplots()
		ax.barh(y = df_stats.index, width = df_stats.stats)
		plt.xlim([0, 250])
		col1.pyplot(fig)
		
		# right column col2 displays the weaknesses and resistances
		# the displayed types are nicely formatted using css (same as earlier)
		col2.subheader('Type Defenses')
		col2.write('Strong Weaknesses (x4)')	
		weakness_text = ''
		for type in weakness_4_types:
			weakness_text += f' <span class="icon type-{type}">{type}</span>'
		col2.markdown(weakness_text, unsafe_allow_html=True)		
		col2.write('Weaknesses (x2)')	
		weakness_text = ''
		for type in weakness_2_types:
			weakness_text += f' <span class="icon type-{type}">{type}</span>'
		col2.markdown(weakness_text, unsafe_allow_html=True)
		
		col2.write('Resistances (x0.5)')
		resistance_half_text = ''
		for type in resistance_half_types:
			resistance_half_text += f' <span class="icon type-{type}">{type}</span>'
		col2.markdown(resistance_half_text, unsafe_allow_html=True)
		
		col2.write('Strong Resistances (x0.25)')
		resistance_quarter_text = ''
		for type in resistance_quarter_types:
			resistance_quarter_text += f' <span class="icon type-{type}">{type}</span>'
		col2.markdown(resistance_quarter_text, unsafe_allow_html=True)


def display_training_breeding(match):	
	# get training data
	catch_rate = match['catch_rate'].iloc[0]
	base_friendship	= match['base_friendship'].iloc[0] 
	base_experience	= match['base_experience'].iloc[0]
	growth_rate = match['growth_rate'].iloc[0]
	
	# get breeding data
	egg_type_number = match['egg_type_number'].iloc[0]
	egg_type_1	= match['egg_type_1'].iloc[0] 
	egg_type_2	= match['egg_type_2'].iloc[0]
	percentage_male = match['percentage_male'].iloc[0]
	egg_cycles = match['egg_cycles'].iloc[0]
		
	with st.container():
		col1, col2 = st.columns(2)
		
		# left column col1 displays training data
		col1.subheader('Training')		
		col1.metric('Catch Rate', catch_rate)
		col1.metric('Base Friendship', base_friendship)
		col1.metric('Base Experience', base_experience)
		col1.metric('Growth Rate', growth_rate)
		
		# right column col2 displays breeding data
		col2.subheader('Breeding')		
		if egg_type_number == 2: # some Pokemon have 2 egg types
			col2.metric('Egg Types', egg_type_1 + ', ' + egg_type_2)
		else:
			col2.metric('Egg Types', egg_type_1)
		if percentage_male != '':	
			percentage_female = str(100 - float(match['percentage_male'].iloc[0]))		
			col2.metric('Percentage Male/Female', percentage_male + '% / ' + percentage_female + '%' )
		else:
			# this metric is not available for Pokemon without eggs, e.g. Mewtwo
			col2.metric('Percentage Male/Female', 'NA')
		col2.metric('Egg Cycles', egg_cycles)
		
  	
def display_radar_chart(match):
	st.header('Radar Chart of Base Stats')
	# get base stats of Pokemon and rename columns nicely
	df_stats = match[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
	df_stats = df_stats.rename(columns={'hp': 'HP', 'attack': 'Attack', 'defense': 'Defense', 'sp_attack': 'Special Attack', 'sp_defense': 'Special Defense', 'speed': 'Speed'}).T
	df_stats.columns=['stats']
	
	# use plotly express to plot out radar char of stats
	fig = px.line_polar(df_stats, r='stats', theta=df_stats.index, line_close=True, range_r=[0, 250])
	st.plotly_chart(fig)
	
	if st.button('Search for Pokemons with Similar Base Stats'):
		display_similar_pokemons(match)


def display_similar_pokemons(match):
	# get base stats of Pokemon and rename columns nicely
	df_stats = match[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
	df_stats = df_stats.rename(columns={'hp': 'HP', 'attack': 'Attack', 'defense': 'Defense', 'sp_attack': 'Special Attack', 'sp_defense': 'Special Defense', 'speed': 'Speed'})
	
	# get stats of all other Pokemon in the full dataframe
	df_stats_all = df[['name', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].set_index('name')
	df_stats_all = df_stats_all.rename(columns={'hp': 'HP', 'attack': 'Attack', 'defense': 'Defense', 'sp_attack': 'Special Attack', 'sp_defense': 'Special Defense', 'speed': 'Speed'})
	
	# find difference between stat of Pokemon and each of the other Pokemons
	diff_df = pd.DataFrame(df_stats_all.values - df_stats.values, index = df_stats_all.index)
	
	# find norm 'distance' between this Pokemon and all other Pokemon
	norm_df = diff_df.apply(np.linalg.norm, axis=1)
	# find 20 other Pokemon with smallest distance, i.e. with most similar base stats to this Pokemon
	similar_pokemons = norm_df.nsmallest(21)[1:22].index # index [1:22] so it does not show itself	
	# store all similar Pokemon with their stats in df
	similar_pokemons_df = df_stats_all.loc[similar_pokemons]
	
	# display name, image, radar chart of each similar Pokemon
	for row in similar_pokemons_df.iterrows():
		name = row[0]
		st.subheader(name) # display Pokemon name
		id = df[df.name == name]['pokedex_number'].iloc[0]
		
		# display Pokemon image
		try:
			path = get_image_path(name, id)
			image = Image.open(path)
			st.image(image)
		except:
			st.write('Image not available.')
		
		# display radar chart	
		fig = px.line_polar(row[1], r=name, theta=row[1].index, line_close=True, range_r=[0, 255])
		st.plotly_chart(fig)
	
	# display full table of all 20 similar Pokemons and their stats
	st.subheader('20 Most Similar Pokemons')
	st.table(similar_pokemons_df)


# calling the functions
display_basic_info(match)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
