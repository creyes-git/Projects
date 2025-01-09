from modules.utils import android_to_hex, validate_csv_df
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe, clear_cache
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


st.set_page_config(page_title = "Cashew Board", page_icon = "🥠", layout = "centered", initial_sidebar_state = "expanded")


load_dotenv()


st.title("_Talk Your Data With_ :green[PandasAI🐼]")
st.write("---")


# Load the Groq Model to use with PandasAI
llm = ChatGroq(model = "llama-3.1-70b-versatile",
               temperature = 0,
               max_tokens = 300,
               max_retries = 2,
               stop_sequences = ["stop", "quit", "exit"])


#with st.sidebar:
#    st.write("If you want to start over, clear the cache:")
#    clear_cache_button = st.button(label = "Clear Chat Cache", help = "Clear the cache and start over")
    
    
if os.path.exists("data/cashew_user_data.csv"): # Read the data if already exists
    
    df = pd.read_csv(r"data/cashew_user_data.csv", engine = "pyarrow", keep_default_na = False)
    
    df_smart = SmartDataframe(df, 
                              name = "My DataFrame", 
                              description = "Brief description of what the dataframe contains",
                              config = {"llm": llm, "enable_cache": False})

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
                df_smart = SmartDataframe(df, 
                              name = "My DataFrame", 
                              description = "Brief description of what the dataframe contains",
                              config = {"llm": llm, "enable_cache": False})
            else:
                st.error(body = "Data validation failed, check your CSV file and try again!", icon = "😢")
                df = pd.DataFrame()
        
        else:
            df = pd.DataFrame()


if df.empty == False:
    user_input = st.chat_input(placeholder = "Ask me anything about your Cashew data...")

    if user_input:
        
        st.chat_message("human").write(user_input)
        os.remove("exports/charts/temp_chart.png") if os.path.exists("exports/charts/temp_chart.png") else None
        
        response = df_smart.chat(query = user_input)
        
        st.chat_message("ai").write(response)
        if os.path.exists("exports/charts/temp_chart.png"):
            st.image(r"exports/charts/temp_chart.png", use_container_width = True, clamp = True)
        
        
#if clear_cache_button:
#    clear_cache()
        