import streamlit as st
import sqlite3

# Connect to the SQLite database containing credit card data
conn = sqlite3.connect("cards.db")
cursor = conn.cursor()

# Define categories and weights for matching (adjust these based on your data)
categories = {
    "income": 2,
    "expenses": -1,
    "travel": 1,
    "rewards": 1,
    "cashback": 1,
    "no_fees": 1,
}

# Streamlit form for user input
with st.form("credit_card_match"):
    income = st.number_input("Annual Income", min_value=0)
    expenses = st.number_input("Monthly Expenses", min_value=0)
    travel_freq = st.selectbox("Travel Frequency", ["None", "Occasional", "Frequent"])
    rewards_pref = st.selectbox("Rewards Preference", ["Cashback", "Travel", "Other"])
    no_fees_pref = st.checkbox("No annual fees preferred?")

    submit_button = st.form_submit_button("Find Matches")

if submit_button:
    # Calculate a score for each card based on user preferences and card data
    scores = {}
    for card in cursor.execute("SELECT * FROM cards"):
        card_id, name, annual_fee, rewards_rate, travel_bonus = card
        score = 0
        for category, weight in categories.items():
            value = getattr(self, category)  # Assuming you have functions to calculate category values
            if category == "no_fees_pref" and no_fees_pref:
                value = 1 if not annual_fee else 0
            score += value * weight
        scores[card_id] = score

    # Sort cards by score and display top matches
    sorted_cards = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    st.header("Top Credit Card Matches")
    for card_id, score in sorted_cards[:5]:  # Display top 5 results
        # Fetch card details and display them along with the score
        card_details = cursor.execute("SELECT * FROM cards WHERE id = ?", (card_id,)).fetchone()
        st.write(f"- {card_details[1]}: Score {score}")

# Close the database connection
conn.close()
