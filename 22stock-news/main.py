# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: https://newsapi.org/
#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# get the first 3 news pieces for the COMPANY_NAME.

import os
import dotenv
import requests
from data import STOCK_DATA
from news import NEWS_DATA
REALTIME_MODE = False

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
dotenv.load_dotenv()

STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")

NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
DIFF_PERCENT_THRESHOLD = 0.1


#1. Get yesterday's closing stock price.
def get_realtime_stock():
    stock_param = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(url=STOCK_ENDPOINT, params=stock_param)
    response.raise_for_status()
    print(response.text)
    _data = response.json()["Time Series (Daily)"] # <class 'dict'>
    print("stock_data:\n", _data)
    return _data

def get_offline_stock():
    return STOCK_DATA["Time Series (Daily)"]

# 2. Get News
def get_realtime_news():
    news_param = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_param)
    news_response.raise_for_status()
    _articles = news_response.json()["articles"]
    print("news:\n",_articles)
    return _articles

def get_offline_news():
    return NEWS_DATA["articles"]

def format_articles(_articles: list) -> list:
    _formatted_articles = []
    for article in _articles:
        if article["author"] is not None and article["description"].strip()!= "" and len(_formatted_articles) < 3:
            _formatted_articles.append(f"Headline: {article["title"]}.\nBrief: {article["description"]}")
    return _formatted_articles



# CHECK REALTIME_MODE to retrieve data realtime from API or local dev files
if REALTIME_MODE:
    stock_data = get_realtime_stock()
    articles = get_realtime_news()
else:
    stock_data = get_offline_stock()
    articles = get_offline_news()

data_list = [value for key, value in stock_data.items()] # get the actual value only
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"yesterday_closing_price: {yesterday_closing_price}")

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"day_before_yesterday_closing_price: {day_before_yesterday_closing_price}")

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
if difference > 0:
    symbol = "🔺"
else:
    symbol = "🔻"

#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((abs(difference) / float(yesterday_closing_price)) * 100, 2)

# Instead of printing ("Get News"), actually
if diff_percent > DIFF_PERCENT_THRESHOLD:
    print(f"diff_percent: {diff_percent} > {DIFF_PERCENT_THRESHOLD} --> Get News!")
    formatted_articles = format_articles(articles)

for item in formatted_articles:
    print(f"\n{STOCK_NAME}: {symbol}{diff_percent}%\n{item}\n")



