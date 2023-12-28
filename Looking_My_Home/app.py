import pandas as pd
import numpy as np
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
from PIL import Image
import requests
import json
import os

#setting the page config
st.set_page_config(page_title="Looking My Home ", page_icon=":house:", layout="wide")

# loading css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# load lottie animation
def lottie_sidebar(path):
    with open(path, "r") as f:
        lottie_home = json.load(f)
    with st.sidebar:
	    st_lottie(lottie_home, height = 100, quality = "high")
     

# calling the api, 1 time per month, saving the data in a csv file and loading it and returning a dataframe
def get_data_and_loaddf():
    #getting the current date
    current_month_year = str(date.today()).split("-")[1] + "-" + str(date.today()).split("-")[0]
    
    # st.secrets call the secret api key from streamlit
    headers = {"accept": "application/json",
            "X-Api-Key": st.secrets["api_key"]}
    
    # list of urls to call
    list_calls = ["https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=1&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=2&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=3&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=4&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=1&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=2&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=3&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=4&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=1&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=2&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=3&status=Active&limit=500",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=4&status=Active&limit=500"]
    
    # checking if the csv file of the current month already exists
    if not os.path.exists(f"Looking_My_Home/rentcast_data_{current_month_year}.csv"):
        df = pd.DataFrame()

        for i in list_calls:
            # calling the api and concatinating in DataFrame
            response = requests.get(i, headers=headers).json()
            df = pd.concat([df, pd.DataFrame(response)], ignore_index=True)
                   
        #saving the dataframe to a csv file       
        df.to_csv(f"Looking_My_Home/rentcast_data_{current_month_year}.csv", index=False)
        
        # creating and cleaning the dataframe
        df = pd.read_csv(f"Looking_My_Home/rentcast_data_{current_month_year}.csv")
    
    else:
        df = pd.read_csv(f"Looking_My_Home/rentcast_data_{current_month_year}.csv")

    df.dropna(subset= ["bathrooms"], how="any", inplace=True)
    df["bathrooms"] = df["bathrooms"].astype(int)
    
    return df

# displaying the scatter map
def display_ga_map(dataframe):
    # Create the scatter mapbox layer
    fig = go.Figure(layout=go.Layout(height=550, width=500))

    fig.add_trace(go.Scattermapbox(
        lat=dataframe['latitude'],
        lon=dataframe['longitude'],
        mode='markers',
        marker=dict(size=7, color = dataframe['price'], cmin=200000, cmax=1000000, colorscale='Sunset', colorbar_title="Price"),
        text=str(dataframe['price'])+"$"))

    # Update the layout of the scatter mapbox
    fig.update_layout(
        mapbox=dict(
            center={"lat": 32.75, "lon": -83.23},
            zoom=5.5,
            style= "carto-positron"))
    
    st.plotly_chart(fig)


# displaying the counties table
def display_counties_ranking(dataframe):
    counties = dataframe[["county", "price"]]
    counties = counties.groupby("county").mean().sort_values("price", ascending=False)
    counties["price"] = counties["price"].astype(int)


    st.dataframe(counties,
                 column_order=("county", "price"),
                 hide_index=False,
                 width=250, height=415,
                 column_config={
                    "county": st.column_config.TextColumn(
                        "County"),
                    "price": st.column_config.ProgressColumn(
                        "Average Price",
                        format="$%d",
                        min_value=0,
                        max_value=max(counties["price"].sort_values(ascending=False)[2:]))})


#sidebar configuration
def call_sidebar():
    with st.sidebar:
        lottie_sidebar("Looking_My_Home/home1.json")
        
        df = get_data_and_loaddf()
        
        st.markdown('<span class="icon type-text">Search</span>' + "  " '<span class="icon type-text2">Your</span>'+ "  "
                    '<span class="icon type-text3">GA</span>' + "  " '<span class="icon type-text4">Property</span>', unsafe_allow_html=True)
       
        st.selectbox("Property Type", df["propertyType"].unique(), index = None, placeholder= "Chose one")
        st.slider("Price Range: ", 0, max(df["price"]), (0, max(df["price"])), format="$%d")
        
        with st.container():
            c1,c2 = st.columns(2)
            c2.radio("Bedrooms: ", df["bedrooms"].sort_values().unique() , index=0)
            c1.radio("Bathrooms: ", df["bathrooms"].sort_values().unique() , index=0)
        
        st.button("Search", type= "primary", on_click= None)
        
        # space
        for i in range(10):
            st.markdown(" ")
        
        with st.container():
            st.write("- :red[**Data Source**]: [RentCast API](https://app.rentcast.io/app)")
            st.write("- :blue[**Info**]: This app only shows Georgia state properties. The data is updated every month")
            st.write("- :green[**Sample limit**]: The sample of the total data is 5000 properties per month")
            st.write("- :orange[**Made by**]: [**Carlos Reyes**](https://github.com/carlosreyes98)")

# Page Configuration and functions calling: #############################################################################################
local_css('Looking_My_Home/style.css')
call_sidebar()
display_counties_ranking(get_data_and_loaddf())
display_ga_map(get_data_and_loaddf())