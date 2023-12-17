import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import requests
import json
import os
from datetime import date
from PIL import Image
from streamlit_lottie import st_lottie

#setting the page config
st.set_page_config(page_title="Looking My Home ", page_icon=":house:", layout="wide")

#getting the current date
current_date = date.today()
# getting the api key from a txt file
with open("C:\\Users\\Carlos Reyes\\Desktop\\rentcast_api_key.txt", "r") as f: 
    api_key = f.read()


list_calls = [
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=1&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=2&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=3&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=4&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=1&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=2&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=3&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=4&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Apartment&bedrooms=1&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Apartment&bedrooms=2&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Apartment&bedrooms=3&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Apartment&bedrooms=4&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=1&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=2&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=3&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=4&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Apartment&bedrooms=1&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Apartment&bedrooms=2&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Apartment&bedrooms=3&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Condo&bedrooms=2&status=Active&limit=500",
            "https://api.rentcast.io/v1/listings/sale?city=Atlanta&state=GA&propertyType=Condo&bedrooms=3&status=Active&limit=500"
            ]

headers = {"accept": "application/json",
           "X-Api-Key": api_key}

#creating an empty dataframe
df = pd.DataFrame()

for i in list_calls:
        #making the call in each url of the list
        response = requests.get(i, headers=headers)
        
        #concatenate the dataframes
        df = pd.concat([df, pd.DataFrame(response.json())], ignore_index=True)
        

#saving the dataframe to a csv file       
df.to_csv('rentcast.csv', index=False)

# charging and cleaning the data
#df = pd.read_csv("C:\\Users\\Carlos Reyes\\Desktop\\rentcast.csv")
#df.drop_duplicates(inplace=True)
#df.dropna(how="all", inplace=True)
