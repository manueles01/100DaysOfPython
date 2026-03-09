import requests
from dotenv import load_dotenv
import os

load_dotenv()




ALPHA_VANTAGE_API_KEY= os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY= os.getenv("NEWS_API_KEY")
STOCK= os.getenv("STOCK")
COMPANY_NAME= os.getenv("COMPANY_NAME")
print(STOCK, COMPANY_NAME)
print("keys loaded:", bool(ALPHA_VANTAGE_API_KEY), bool(NEWS_API_KEY))

AV_URL = "https://www.alphavantage.co/query"

av_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}

av_response = requests.get(AV_URL, params=av_params)
av_response.raise_for_status()
data = av_response.json()

time_series = data["Time Series (Daily)"]
dates = list(time_series.keys())

yesterday_close = float(time_series[dates[0]]["4. close"])
day_before_close = float(time_series[dates[1]]["4. close"])

difference = yesterday_close - day_before_close
pct_change = round((difference/day_before_close)*100,2)

if abs(pct_change) >= 0.1:
    arrow = "🔺" if difference > 0 else "🔻"
    print(f"{STOCK}: {arrow}{abs(pct_change)}%")
    NEWS_URL = "https://newsapi.org/v2/everything"

    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3
    }

    news_response = requests.get(NEWS_URL, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()

    articles = news_data["articles"]

    for article in articles:
        print(f"\n{STOCK}: {arrow}{abs(pct_change)}%")
        print(f"Headline: {article['title']}")
        print(f"Brief: {article['description']}")
else:
    print(f"Change of {pct_change}% is under threshold, no news needed.")

print(f"Yesterday: {yesterday_close}")
print(f"Day before: {day_before_close}")
print(f"Change: {pct_change}")


#STOCK = "TSLA"
#COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

