from newsapi import NewsApiClient
from datetime import datetime, timedelta
import os

api = NewsApiClient(api_key = os.getenv('NEWS_API_KEY'))

last_week = (datetime.today() - timedelta(days = 7)).strftime("%Y-%m-%d")


def get_weekly_news(keyword, category):
    
    response = api.get_top_headlines(q = keyword, category = category.lower(), country = "us")
    news_list = []
    
    for i in response["articles"]:
        news_list.append(i["description"])
    
    return news_list