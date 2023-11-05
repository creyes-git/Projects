import requests
import pandas as pd
import numpy as np

#using rentcast api to get the data, this api key has 250 as limit per call,
#so I will need to call it more than once to get all the data
#i will call by amount of bedrooms

list_calls = ["https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Condo&bedrooms=1&status=Active&limit=500",
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
              "https://api.rentcast.io/v1/listings/sale?state=GA&propertyType=Single%20Family&bedrooms=4&status=Active&limit=500"]

headers = {"accept": "application/json",
           "X-Api-Key": "your_api_key_here"}

#creating an empty dataframe
df = pd.DataFrame()

for i in list_calls:
        #making the call in each url of the list
        response = requests.get(i, headers=headers)
        
        #concatenate the dataframes
        df = pd.concat([df, pd.DataFrame(response.json())], ignore_index=True)
        

#saving the dataframe to a csv file       
df.to_csv('rentcast.csv', index=False)

#cleaning the data
df = pd.read_csv("C:\\Users\\Carlos Reyes\\Desktop\\rentcast.csv")
df.drop(["removedDate"],inplace=True,axis=1)
df.dropna(how="all", inplace=True)
df.drop_duplicates(inplace=True)
