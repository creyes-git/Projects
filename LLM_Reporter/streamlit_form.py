import streamlit as st
import sqlite3 as sql
from re import match


def validate_email(email):
    if match(r"^[a-z0-9]{1,48}@gmail\.com$", email):
        return True
    else:
        return False


st.set_page_config(page_icon = "📩",page_title = "PyInbox", layout = "centered", initial_sidebar_state = "collapsed")


st.warning("Please fill out the form below with your personal information to subscribe to PyInbox Newsletter.")


with st.form(key = "newsletter_form", clear_on_submit = True):
    
    name = st.text_input(label = "User Name: ")
    
    age = st.number_input(label = "User Age: ", min_value = 18, max_value = 100, help = "Please enter your age, this will be used to personalize your News Feed.")
    
    email = st.text_input(label = "User Gmail: ", help = "Please enter a valid email address. For now we only support Gmail accounts.")
    
    st.write("Newsletter Preferences: ")
    
    category = st.selectbox(label = "Category", 
                            options = ['Business', 'Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology'], 
                            help = "Select the category of news you want to receive.")
    
    keyword = st.text_input(label = "Keyword: ", max_chars = 20, help = "Enter the Keyword(maximum of 20 characters), that you want to use to perzonalize your News Feed. Example: Trump, Cats, Bitcoin.")
    
    
    submit_button = st.form_submit_button(label = "Submit", type = "primary", icon = "✅")
    

# Validate the email and Saving the user data 
if submit_button:
    
    if validate_email(email):
        connection = sql.connect(r"data/PyInbox.db")
        cursor = connection.cursor()
        
        cursor.execute("CREATE TABLE IF NOT EXISTS users (Name, Email, Age, Category, Keyword)")
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (name, email, age, category, keyword))
        
        connection.commit()
        connection.close()
        
        st.balloons()
        st.success("You have successfully subscribed to PyInbox Newsletter.", icon = "✅")
    
    else:
        st.warning("Please enter a valid email address.", icon = "⚠️")