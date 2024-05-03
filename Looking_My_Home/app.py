import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import json
import requests
import os
import config

#setting the page config and creating the functions
st.set_page_config(page_title="My Home in GA", page_icon=":house:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css('style.css')

#FUNCTIONS:
# calling the api, 1 time per month, saving the data in a csv file and loading it and returning a dataframe
def get_data_and_loaddf():
    #getting the current date
    current_month_year = str(date.today()).split("-")[1] + "-" + str(date.today()).split("-")[0]
    
    # st.secrets call the secret api key from streamlit
    headers = {"accept": "application/json",
                "X-Api-Key": os.environ.get('API_KEY')}
    
    # list of urls to call
    list_calls = [
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=1&status=Active&limit=500",
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
                "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=4&status=Active&limit=500"
                ]
    
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
        
# displaying the scatter map
def display_ga_map(dataframe):
    # Create the scatter mapbox layer
    fig = go.Figure(layout=go.Layout(height=500, width=530))

    fig.add_trace(go.Scattermapbox(
        lat=dataframe['latitude'],
        lon=dataframe['longitude'],
        mode='markers',
        marker=dict(size=7, color = dataframe['price'], cmin=200000, cmax=1000000, colorscale="Viridis_r", colorbar_title="Price"),
        text=str(dataframe['price'])+"$"))

    # Update the layout of the scatter mapbox
    fig.update_layout(
        title='Georgia Properties Scatter Map',
        mapbox=dict(
            center={"lat": 33, "lon": -82.90},
            zoom=5.30,
            style= "carto-positron"))
    
    st.plotly_chart(fig, use_container_width=True)

# displaying the counties table
def display_counties_ranking(dataframe):
    counties = dataframe[["county", "price"]]
    counties = counties.groupby("county").mean().sort_values("price", ascending=False)
    counties["price"] = counties["price"].astype(int)

    with st.container():
        st.markdown("**Average Price per County**")
        st.dataframe(data=counties,
                        column_order=("county", "price"),
                        hide_index=False,
                        width=430, height=385,
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

    fig = px.scatter(dataframe, x ="squareFootage" , y="price", width=580, height=500, color="propertyType",
                    color_discrete_sequence=["#a9dc67", "#4b780b", "#fed947"], hover_name="addressLine1", 
                    hover_data=["city","daysOnMarket", "yearBuilt", "bathrooms", "bedrooms"])
    
    fig.update_layout(
        xaxis_title="Square Footage",
        yaxis_title="Price($)",
        legend_title="Property Type",
        title = "         Relationship / Square Footage & Price")
    
    st.write(" ")
    st.write(" ")
    st.plotly_chart(fig)

# get average properties stats of price, bathrooms, bedrooms, days on market and size
def display_avg_stats(dataframe):
    if dataframe["price"].values.any():
        avg_price = dataframe["price"].values.mean().astype(int).round(-3)
    else:
        avg_price = None
    if dataframe["squareFootage"].values.any():
        avg_size = dataframe["squareFootage"].dropna(how="any").values.mean().astype(int)
    else:
        avg_size = None
    if dataframe["bedrooms"].values.any():
        avg_beds = dataframe["bedrooms"].values.mean().astype(int)
    else:
        avg_beds = None
    if dataframe["daysOnMarket"].values.any():
        avg_days_market = dataframe["daysOnMarket"].values.mean().astype(int)
    else:
        avg_days_market = None
    
    with st.container():
            c1, c2, c3, c4 = st.columns(4)
            c1.metric(f" :orange[**Average Price($)**]", f"{str(avg_price)}")
            c2.metric(f" :orange[**Average Size(sqft)**]", f"{str(avg_size)}")
            c3.metric(f" :orange[**Average Days on Market**]", f"{str(avg_days_market)}")
            c4.metric(f" :orange[**Bedrooms**]", f"{str(avg_beds)}")
            
def display_type_pie(dataframe):
    df = dataframe.groupby("propertyType")["propertyType"].count().rename("Count").reset_index()
    if df.values.any():
        with st.container():
            st.plotly_chart(px.pie(df, values="Count",names="propertyType", title="Property Type Distribution", height=455, width=570,
                            color_discrete_sequence=px.colors.sequential.Aggrnyl_r, hole=0.5))
    else:
        st.plotly_chart(px.pie(values=[1],names=["No property"], title="No property found in your search", hole=0.5, height=455, width=570))

# DASHBOARD CALLING:
st.warning("Welcome to 'My Home in GA Dashboard'. Check the Georgia Properties Market information and filter the results based on your preferences :smile:! ")
temp_df = get_data_and_loaddf()
    
#sidebar configuration
with st.sidebar:
    
    st_lottie(json.load(open("home1.json")), height = 100, quality = "high")
     
    st.markdown('<span class="icon type-red">Search</span>' + "  " '<span class="icon type-yellow">Your</span>'+ "  "
                '<span class="icon type-normal">GA</span>' + "  " '<span class="icon type-green">Property</span>', unsafe_allow_html=True)
       
    prop_type = st.selectbox("Property Type", temp_df["propertyType"].unique(), index = None, placeholder= "Chose one:")
    county = st.selectbox("County", temp_df["county"].unique(), index = None, placeholder= "Search your county:")
    price_range = st.slider("Price Range: ", 0, max(temp_df["price"]), (0, max(temp_df["price"])), format="$%d")
        
    with st.container():
        beds = st.radio("Bedrooms: ", temp_df["bedrooms"].sort_values().unique() , index=0)
        
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

df = get_data_and_loaddf()
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

# CALLING FUNCTIONS       
display_avg_stats(df)
c1, c2 = st.columns(2)
with c1:
    display_ga_map(df)
    display_counties_ranking(df)
with c2:
    display_type_pie(df)
    display_scatter_map(df)