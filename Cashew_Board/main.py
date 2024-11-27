from scripts.utils import android_to_hex
from scripts.plotly_charts import *
import streamlit as st
import pandas as pd
import os


st.set_page_config(page_title = "Cashew Board", page_icon = "🥠", layout = "wide", initial_sidebar_state = "expanded") # Setting Streamlit Main Page Config


with open("assets/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True) # Setting Custom CSS


data_folder = r"/workspaces/Projects/Cashew_Board/data"
file_on_folder = os.listdir(data_folder)[0]

df = pd.read_csv(fr"{data_folder}/{file_on_folder}", engine = "pyarrow", keep_default_na = False)
df["color"] = df["color"].apply(android_to_hex) # Transform color code to hex
df['amount'] = df['amount'].abs() # Transform negative values to positive
df["date"] = pd.to_datetime(df["date"].dt.strftime("%m-%d-%Y")) # Format date to keep only month-day-year


with st.sidebar:
    c1, c2 = st.columns(2)
    c1.markdown('<span class="bubble type-beiche">Welcome</span>', unsafe_allow_html = True)
    c1.markdown('<span class="bubble type-blue">TO</span>', unsafe_allow_html = True)
    c1.markdown('<span class="bubble type-green">Cashew</span>', unsafe_allow_html = True)
    c1.markdown('<span class="bubble type-red">Board</span>', unsafe_allow_html = True)

    c2.image("assets/images/icon.png", width = 115, clamp = True)
    st.markdown("---")
    #st.image("assets/images/empty.png", use_column_width = True)
    

with st.container():
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f'<span class="bubble-container type-red">Max Spend: ${df[df["income"] == False]["amount"].max():,.0f}</span>', unsafe_allow_html = True)
    c2.markdown(f'<span class="bubble-container type-green">Max Income: ${df[df["income"] == True]["amount"].max():,.0f}</span>', unsafe_allow_html = True)
    c3.markdown(f'<span class="bubble-container type-blue">Start Date: {df["date"].min().strftime("%m-%d-%Y")}</span>', unsafe_allow_html = True)
    c4.markdown(f'<span class="bubble-container type-beiche">Total Transactions: {len(df)}</span>', unsafe_allow_html = True)
    

# PLOTLY CHARTS------------------------------------------------------------------------------------------------------------------------------------------------------------
st.plotly_chart(plot_hist_income_expense(df), use_container_width = True) # Histogram Income vs Expense + Saving

with st.container():
    c1, c2 = st.columns(2)
    c2.plotly_chart(plot_saving_rate(df), use_container_width = True)
    
with st.container(): # Categories Charts Container
    c1, c2 = st.columns(2)
    category = c1.selectbox(label = "", options = df[df["income"] == False]["category name"].unique(), index = None) # Select Expense Category
    c1.image(plot_category_map(df, category), use_column_width = True)
    c2.plotly_chart(plot_pie_categories(df), use_container_width = True)