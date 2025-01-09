from modules.utils import android_to_hex, validate_csv_df
from modules.plotly_charts import *
import streamlit as st
from pandasai import SmartDataframe
from langchain_groq import ChatGroq
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()


st.set_page_config(page_title = "Cashew Board", page_icon = "🥠", layout = "wide", initial_sidebar_state = "expanded")


st.title("_Talk Your Data With_ :green[PandasAI🐼]")
st.write("---")


llm = ChatGroq(model = "llama-3.1-70b-versatile",
               temperature = 1,
               max_tokens = 300,
               max_retries = 2,
               stop_sequences = ["stop", "quit", "exit"])


if os.path.exists("data/cashew_user_data.csv"): # Read the data if already exists
    
    df = pd.read_csv(r"data/cashew_user_data.csv", engine = "pyarrow", keep_default_na = False)
    
    df_smart = SmartDataframe(df, 
                              name = "My DataFrame", 
                              description = "Brief description of what the dataframe contains",
                              config={"llm": llm})

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


user_input = st.chat_input(placeholder = "Ask me anything about your Cashew data...")

if user_input:
    
    st.chat_message("human").write(user_input)
    
    response = df_smart.chat(query = user_input)
    st.chat_message("ai").write(response)