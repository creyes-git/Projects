from newsapi import NewsApiClient
import os

api = NewsApiClient(api_key = os.getenv('NEWS_API_KEY'))

def get_weekly_news(keyword = None, category = None):
    
    response = api.get_top_headlines(q = keyword, category = category, country = "us")
    news_list = ""
    n = 1
    
    for i in response["articles"]:
        
        description = i["description"]
        
        if description and description != "[Removed]":
        
            news_list += str(n) + "-" + description + "\n"
            n += 1
        
        else:
            continue
    
    return news_list