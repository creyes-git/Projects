import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import requests
import json
import os

#setting the page config and creating the functions
st.set_page_config(page_title="Looking My Home ", page_icon=":house:", layout="wide")

# calling the api, 1 time per month, saving the data in a csv file and loading it and returning a dataframe
def get_data_and_loaddf():
    #getting the current date
    current_month_year = str(date.today()).split("-")[1] + "-" + str(date.today()).split("-")[0]
    
    # st.secrets call the secret api key from streamlit
    headers = {"accept": "application/json",
            "authorization": "32f4a4cf6b4b4078b8f00d0bd185d850"}
    
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
        
    df.dropna(subset= "bathrooms", how="any", inplace=True)
    df["bathrooms"] = df["bathrooms"].astype(int)
    
    return df

# displaying the scatter map
def display_ga_map(dataframe):
    # Create the scatter mapbox layer
    fig = go.Figure(layout=go.Layout(height=500, width=500))

    fig.add_trace(go.Scattermapbox(
        lat=dataframe['latitude'],
        lon=dataframe['longitude'],
        mode='markers',
        marker=dict(size=7, color = dataframe['price'], cmin=200000, cmax=1000000, colorscale='Sunset', colorbar_title="Price"),
        text=str(dataframe['price'])+"$"))

    # Update the layout of the scatter mapbox
    fig.update_layout(
        title='Georgia Properties Scatter Map',
        mapbox=dict(
            center={"lat": 33, "lon": -82.90},
            zoom=5.30,
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

def display_scatter_map(dataframe):
    dataframe = dataframe[dataframe["squareFootage"] <= 10000]
    dataframe = dataframe[dataframe["price"] <= 7500000] 

    fig = px.scatter(dataframe, x ="squareFootage" , y="price", width=500, height=500, color="propertyType",
                    color_discrete_sequence=["red", "green", "orange"], hover_name="addressLine1", 
                    hover_data=["city","daysOnMarket", "yearBuilt", "bathrooms", "bedrooms"])
    
    fig.update_layout(
        xaxis_title="Square Footage",
        yaxis_title="Price($)",
        legend_title="Property Type",
        title = "         Relationship / Square Footage & Price")
    

    return st.plotly_chart(fig)

# get average properties stats of price, bathrooms, bedrooms, days on market and size
def display_avg_stats(dataframe):
    
    avg_price = dataframe["price"].values.mean().astype(int).round(-3)
    avg_size = dataframe["squareFootage"].dropna(how="any").values.mean().astype(int)
    avg_beds = dataframe["bedrooms"].values.mean().astype(int)
    avg_baths = dataframe["bathrooms"].values.mean().astype(int)
    avg_days_market = dataframe["daysOnMarket"].values.mean().astype(int)
    
    with st.container():
            st.metric(f" :red[**Average Price**]", f"{str(avg_price)}$",)
            st.metric(f" :blue[**Average Size**]", f"{str(avg_size)} sqft")
            st.metric(f" :green[**Bedrooms/Bathrooms**]", f"{str(avg_beds)}/{str(avg_baths)}")
            st.metric(f" :orange[**Average Days on Market**]", f"{str(avg_days_market)} days")


st.dataframe(get_data_and_loaddf())