from email_sender import send_email
from groq_summarize import summarize_news
from news_api import get_weekly_news
from datetime import datetime, timedelta
import sqlite3 as sql
import pandas as pd


today = datetime.today().strftime("%m-%d")
last_week = (datetime.today() - timedelta(days = 7)).strftime("%m-%d")


connection = sql.connect("PyInbox/data/PyInbox.db")
cursor = connection.cursor()

df_users = pd.DataFrame(cursor.execute("SELECT * FROM users"), columns = [i[0] for i in cursor.description])

connection.commit()
connection.close()


for i in df_users.index:
    
    email = df_users["Email"][i]
    name = df_users["Name"][i]
    category = df_users["Category"][i]
    keyword = df_users["Keyword"][i]
    
    
    top_news = get_weekly_news(keyword = keyword, category = category.lower())
    
    
    llm_summary = summarize_news(top_news)
    
    
    send_email(title = f"PyInbox Weekly News for {last_week} TO {today}",
               email_receiver = email, 
               body = f'''Hello {str(name.split()[0]).capitalize()}!\n\n{llm_summary}\n\nBest regards, have a great week!''')