import streamlit as st
import sqlite3 as sql
from email_validator import validate_email, EmailNotValidError
import re


st.set_page_config(page_icon = "📩",page_title = "PyInbox", layout = "centered", initial_sidebar_state = "collapsed")


with st.form(key = "newsletter_form", clear_on_submit = True):
    
    name = st.text_input(label = "User Name: ")
    
    email = st.text_input(label = "User Email: ")
    
    age = st.number_input(label = "User Age: ", min_value = 18, max_value = 100, help = "Please enter your age, this will be used to personalize your News Feed.")
    
    
    st.write("Newsletter Preferences: ")
    
    category = st.selectbox(label = "Category", 
                            options = ['Business', 'Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology'], 
                            help = "Select the category of news you want to receive.")
    
    keyword = st.text_input(label = "Keyword: ", max_chars = 30, help = "Enter the keyword you want to perzonalize even more your News Feed")
    
    
    submit = st.form_submit_button(label = "Submit", type = "primary", icon = "📩")