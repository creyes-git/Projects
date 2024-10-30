from index import *
import streamlit as st


st.set_page_config(page_title="OpenDash", page_icon=":stock:", layout = "centered", initial_sidebar_state = "expanded")


with st.sidebar:
    select_index = st.selectbox("Index", get_index_symbols().unique())
    
    show_chart = st.button("Show Chart", type = "primary")
    
    
if show_chart:
    st.line_chart(get_index_hprice(select_index), use_container_width = True)
    