from scripts.plotly_charts import *
import streamlit as st
import pandas as pd
import os


st.set_page_config(page_title = "Cashew Board", page_icon = ":moneybag:", layout = "wide", initial_sidebar_state = "expanded")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css('assets/style.css')


def android_to_hex(color_code):
    hex_code = "#{:06x}".format(color_code & 0xffffff)
    return hex_code


data_folder = r"/workspaces/Projects/Cashew_Board/data"
file_on_folder = os.listdir(data_folder)[0]

df = pd.read_csv(fr"{data_folder}/{file_on_folder}", engine = "pyarrow", keep_default_na = False)
df["color"] = df["color"].apply(android_to_hex)
df['amount'] = df['amount'].abs() # Transform negative values to positive


with st.sidebar:
    c1, c2 = st.columns(2)
    c1.markdown('<span class="icon type-beiche">Welcome</span>', unsafe_allow_html = True)
    c1.markdown('<span class="icon type-blue">TO</span>', unsafe_allow_html = True)
    c1.markdown('<span class="icon type-green">Cashew</span>', unsafe_allow_html = True)
    c1.markdown('<span class="icon type-red">Board</span>', unsafe_allow_html = True)

    c2.image("assets/images/icon.png", width = 115, clamp = True)
    st.markdown("---")
    #st.image("assets/images/empty.png", use_column_width = True)