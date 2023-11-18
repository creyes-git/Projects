import pandas as pd
import requests

url = "https://narutodb.xyz/api/character?page=1&limit=1431"

#Dataframe:
response = requests.get(url).json()
df = pd.DataFrame(response["characters"])
df.drop(columns=df.columns[12:], inplace=True)
