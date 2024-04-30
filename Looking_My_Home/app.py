import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import requests
import os

#setting the page config and creating the functions
st.set_page_config(page_title="Looking My Home ", page_icon=":house:", layout="wide")

# calling the api, 1 time per month, saving the data in a csv file and loading it and returning a dataframe
def get_data_and_loaddf():
    #getting the current date
    current_month_year = str(date.today()).split("-")[1] + "-" + str(date.today()).split("-")[0]
    
    # st.secrets call the secret api key from streamlit
    headers = {"accept": "application/json",
                "X-Api-Key": "9f3c938b8f2844ef88bc452bd9262e43"}
    
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
    if os.path.exists(f"Looking_My_Home/rentcast_data_{current_month_year}.csv"):
        
        df = pd.read_csv(f"Looking_My_Home/rentcast_data_{current_month_year}.csv")
           
    else:
        df = pd.DataFrame()

        for i in list_calls:
            # calling the api and concatinating in DataFrame
            response = requests.get(i, headers=headers).json()
            df = pd.concat([df, pd.DataFrame(response)], ignore_index=True)
                   
        #saving the dataframe to a csv file       
        df.to_csv(f"Looking_My_Home/rentcast_data_{current_month_year}.csv", index=False)
        
        # creating and cleaning the dataframe
        df = pd.read_csv(f"Looking_My_Home/rentcast_data_{current_month_year}.csv")
       
    df.dropna(subset= "bathrooms", how="any", inplace=True)
    df["bathrooms"] = df["bathrooms"].astype(int)
    
    return df

st.dataframe(get_data_and_loaddf())