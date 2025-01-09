from modules.utils import android_to_hex, validate_csv_df
from modules.plotly_charts import *
import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer
import os


st.set_page_config(page_title = "Cashew Board", page_icon = "🥠", layout = "wide", initial_sidebar_state = "expanded")


st.title("_Explore Your Data With_ :orange[Pygwalker🕊]")
st.write("---")

if os.path.exists("data/cashew_user_data.csv"): # Read the data if already exists
    
    df = pd.read_csv(r"data/cashew_user_data.csv", engine = "pyarrow", keep_default_na = False)

else:
    with st.sidebar:
        
        # READ CASH APP CSV TO DATAFRAME
        cashew_csv_file = st.file_uploader(label = "Your Cashew CSV Data Here", type = ["csv"], accept_multiple_files = False, help = "Go to Cashew App > Settings > Export Data > Export CSV")
        
        if cashew_csv_file:
            df = pd.read_csv(cashew_csv_file, engine = "pyarrow", keep_default_na = False)
            df["color"] = df["color"].apply(android_to_hex) # Transform color code to hex
            df['amount'] = df['amount'].abs() # Transform negative values to positive
            df["date"] = pd.to_datetime(df["date"].dt.strftime("%m-%d-%Y")) # Format date to keep only month-day-year
            
            if validate_csv_df(df): # Validate CSV Columns
                st.success(body = "Data Loaded Successfully!", icon = "🥳")
            else:
                st.error(body = "Data validation failed, check your CSV file and try again!", icon = "😢")
                df = pd.DataFrame()
        
        else:
            df = pd.DataFrame()


if df.empty == False:
    pyg_app = StreamlitRenderer(df)
    
    pyg_app.explorer()
    
else:
    st.warning("No data to display, please upload your Cashew CSV file to get started!🚀")