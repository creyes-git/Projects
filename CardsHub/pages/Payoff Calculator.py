import streamlit as st

monthly_payment = st.number_input("Monthly payment: ", min_value = 0)
interest_rate = st.number_input("Interest rate: ", min_value = 0)
