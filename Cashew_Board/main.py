from scripts.utils import android_to_hex, validate_csv_df
from scripts.plotly_charts import *
import streamlit as st
import pandas as pd


st.set_page_config(page_title = "Cashew Board", page_icon = "🥠", layout = "wide", initial_sidebar_state = "expanded") # Setting Streamlit Main Page Config


with open("assets/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True) # Setting Custom CSS


# SIDEBAR------------------------------------------------------------------------------------------------------------------------------------------------------------
with st.sidebar:
    c1, c2 = st.columns(2)
    
    c2.markdown('<span class="bubble type-beiche">Welcome</span>', unsafe_allow_html = True)
    c2.markdown('<span class="bubble type-blue">TO</span>', unsafe_allow_html = True)
    c2.markdown('<span class="bubble type-green">Cashew</span>', unsafe_allow_html = True)
    c2.markdown('<span class="bubble type-red">Board</span>', unsafe_allow_html = True)

    c1.image("assets/images/icon.png", width = 115, clamp = True)
    st.markdown("---")
    
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
    # MAIN PAGE------------------------------------------------------------------------------------------------------------------------------------------------------------
    with st.container(): # Main Page Header Container
        c1, c2, c3, c4 = st.columns(4)
        c1.markdown(f'<span class="bubble-container type-red">Max Spend: ${df[df["income"] == False]["amount"].max():,.0f}</span>', unsafe_allow_html = True)
        c2.markdown(f'<span class="bubble-container type-green">Max Income: ${df[df["income"] == True]["amount"].max():,.0f}</span>', unsafe_allow_html = True)
        c3.markdown(f'<span class="bubble-container type-blue">Start Date: {df["date"].min().strftime("%m-%d-%Y")}</span>', unsafe_allow_html = True)
        c4.markdown(f'<span class="bubble-container type-beiche">Total Transactions: {len(df)}</span>', unsafe_allow_html = True)
        
        
    # Plotly Charts
    st.plotly_chart(plot_hist_income_expense(df), use_container_width = True) # Histogram Income vs Expense + Saving

    with st.container():
        c1, c2 = st.columns(2)
        c1.plotly_chart(plot_income_funnel(df), use_container_width = True)
        c2.plotly_chart(plot_saving_rate(df), use_container_width = True)
        
    with st.container(): # Categories Charts Container
        c1, c2 = st.columns(2)
        category = c1.selectbox(label = "", options = df[df["income"] == False]["category name"].unique(), index = None) # Select Expense Category
        c1.image(plot_category_map(df, category), use_container_width = True)
        c2.plotly_chart(plot_pie_categories(df), use_container_width = True)
        
else:
    c1, c2, c3, c4, c5 = st.columns(5)
    c2.title("_Upload Your_")
    c3.title(":orange[CASHEW]:sunglasses:")
    c4.title("_CSV To Start_")
    c2.write("\n")
    c1, c2, c3 = st.columns(3)
    c2.image("assets/images/no-search.png")