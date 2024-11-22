import pandas as pd 
import plotly.graph_objects as go
from datetime import datetime
import os

data_folder = r"/workspaces/Projects/Cashew_Board/data"
file_on_folder = os.listdir(data_folder)[0]

def android_to_hex(color_code):
    hex_code = "#{:06x}".format(color_code & 0xffffff)
    return hex_code

df = pd.read_csv(fr"{data_folder}/{file_on_folder}", engine = "pyarrow", keep_default_na = False)
df["color"] = df["color"].apply(android_to_hex)
df['amount'] = df['amount'].abs() # Transform negative values to positive
df["date"] = df["date"].dt.strftime("%Y-%m")