import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import json
import requests
import os

#setting the page config and creating the functions
st.set_page_config(page_title="My Home in GA", page_icon=":house:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# load cssp
local_css('style.css')

# calling the api, 1 time per month, saving the data in a csv file and loading it and returning a dataframe
def get_data_and_loaddf():
    #getting the current date
    current_month_year = str(date.today()).split("-")[1] + "-" + str(date.today()).split("-")[0]
    
    # st.secrets call the secret api key from streamlit
    headers = {"accept": "application/json",
                "X-Api-Key": "b047031a86a545b7bb6e5d5a82ce6d95"}
    
    # list of urls to call
    list_calls = [
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=1&status=Active&limit=500&offset=0",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=2&status=Active&limit=500&offset=1000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=3&status=Active&limit=500&offset=10000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=4&status=Active&limit=500&offset=20000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=1&status=Active&limit=500&offset=30000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=2&status=Active&limit=500&offset=40000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=3&status=Active&limit=500&offset=50000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=4&status=Active&limit=500&offset=60000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=1&status=Active&limit=500&offset=70000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=2&status=Active&limit=500&offset=80000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=3&status=Active&limit=500&offset=90000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=4&status=Active&limit=500&offset=100000",
                
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=1&status=Active&limit=500&offset=15000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=2&status=Active&limit=500&offset=160000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=3&status=Active&limit=500&offset=100000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=4&status=Active&limit=500&offset=200000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=1&status=Active&limit=500&offset=300000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=2&status=Active&limit=500&offset=400000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=3&status=Active&limit=500&offset=500000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=4&status=Active&limit=500&offset=600000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=1&status=Active&limit=500&offset=700000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=2&status=Active&limit=500&offset=800000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=3&status=Active&limit=500&offset=900000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=4&status=Active&limit=500&offset=1000000",
                
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=1&status=Active&limit=500&offset=155555",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=2&status=Active&limit=500&offset=150000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=3&status=Active&limit=500&offset=1000000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=4&status=Active&limit=500&offset=2000000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=1&status=Active&limit=500&offset=3000000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=2&status=Active&limit=500&offset=4000000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=3&status=Active&limit=500&offset=5000000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=4&status=Active&limit=500&offset=6000000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=1&status=Active&limit=500&offset=7000000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=2&status=Active&limit=500&offset=8000000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=3&status=Active&limit=500&offset=9000000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=4&status=Active&limit=500&offset=10000000",
                
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=1&status=Active&limit=500&offset=180000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=2&status=Active&limit=500&offset=190000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=3&status=Active&limit=500&offset=1200000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=4&status=Active&limit=500&offset=2200000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=1&status=Active&limit=500&offset=3200000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=2&status=Active&limit=500&offset=4100000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=3&status=Active&limit=500&offset=510000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Townhouse&bedrooms=4&status=Active&limit=500&offset=6100000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=1&status=Active&limit=500&offset=7100000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=2&status=Active&limit=500&offset=8100000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=3&status=Active&limit=500&offset=9100000",
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=4&status=Active&limit=500&offset=11000000"]
    
    # checking if the csv file of the current month already exists
    if os.path.exists(f"rentcast_data_{current_month_year}.csv"):
        df = pd.read_csv(f"rentcast_data_{current_month_year}.csv")
             
    else:
        df = pd.DataFrame()

        for i in list_calls:
            # calling the api and concatinating in DataFrame
            response = requests.get(i, headers=headers).json()
            df = pd.concat([df, pd.DataFrame(response)], ignore_index=True)
                   
        #saving the dataframe to a csv file       
        df.to_csv(f"rentcast_data_{current_month_year}.csv", index=False)
        # creating and cleaning the dataframe
        df = pd.read_csv(f"rentcast_data_{current_month_year}.csv")
       
    df.dropna(subset= "bathrooms", how="any", inplace=True)
    df["bathrooms"] = df["bathrooms"].astype(int)
    
    return df


#sidebar configuration
with st.sidebar:
    df = get_data_and_loaddf()
    
    st_lottie(json.load(open("home1.json")), height = 100, quality = "high")
     
    st.markdown('<span class="icon type-red">Search</span>' + "  " '<span class="icon type-yellow">Your</span>'+ "  "
                '<span class="icon type-normal">GA</span>' + "  " '<span class="icon type-green">Property</span>', unsafe_allow_html=True)
       
    prop_type = st.selectbox("Property Type", df["propertyType"].unique(), index = None, placeholder= "Chose one:")
    county = st.selectbox("County", df["county"].unique(), index = None, placeholder= "Search your county:")
    price_range = st.slider("Price Range: ", 0, max(df["price"]), (0, max(df["price"])), format="$%d")
        
    with st.container():
        c1,c2 = st.columns(2)
        beds = c2.radio("Bedrooms: ", df["bedrooms"].sort_values().unique() , index=0)
        baths = c1.radio("Bathrooms: ", df["bathrooms"].sort_values().unique() , index=0)  
    
    st.markdown(" ")
    # button
    button = st.button("**Filter & Search**", type= "primary")
    
    st.markdown("---")
    # Info and sources
    with st.container():
        st.write("- :red[**Data Source**]: [RentCast API](https://app.rentcast.io/app)")
        st.write("- :blue[**Info**]: This app only shows Georgia state properties. The data is updated every month")
        st.write("- :green[**Sample limit**]: The sample of the total data is 5000 properties per month")
        st.write("- :orange[**Made by**]: [**Carlos Reyes**](https://github.com/carlosreyes98)")
        
# button!!!      
if button:
    # dataset configuration
    if prop_type is not None:
        df = df[df["propertyType"] == prop_type]
    if county is not None:
        df = df[df["county"] == county]
    if price_range is not None:
        df = df[(df["price"] >= price_range[0]) & (df["price"] <= price_range[1])]
    if beds is not None:
        df = df[df["bedrooms"] == beds]
    if baths is not None:
        df = df[df["bathrooms"] == baths]
    
    
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


# DASHBOARD CALLING:
with st.container():
    c1, c2, c3, c4 = st.columns(4)
    cc1, cc2, cc3 = st.columns(3)
    with c2:
        st.markdown(" Basic Property Stats:  ")
        display_avg_stats(df)
    with c1:
        st.markdown(" AVG Price County Ranking:  ")
        display_counties_ranking(df)
        
with st.container():
    c1, c2 = st.columns(2)
    with c2:
        display_scatter_map(df)
    with c1:
        display_ga_map(df)