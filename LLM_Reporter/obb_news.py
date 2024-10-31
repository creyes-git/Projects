from openbb import obb
from datetime import datetime, timedelta
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

obb.user.credentials.tiingo_token = "aac0353367e16bc038f4b460f150f36e02eead94"

last_week = (datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d")


news = obb.news.world(start_date = last_week, provider = "tiingo")

df_news = news.to_dataframe()

print(df_news)