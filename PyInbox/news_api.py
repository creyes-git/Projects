from newsapi import NewsApiClient
from datetime import datetime, timedelta
import pandas as pd
import os

newsapi = NewsApiClient(api_key = os.getenv('NEWS_API_KEY'))

last_week = (datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d")


def get_df_weekly_news(keyword, category):
    
    news = newsapi.get_top_headlines(q = keyword, category = category.lower(), country = "us")
    
    df = pd.DataFrame(news["articles"])
    #df = df[["title", "description", "url", "urlToImage"]]
    
    return df

df = get_df_weekly_news("Trump", "Business")

print(df)