import requests
import pprint

from newsapi import NewsApiClient
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "E08DWT9C2ZKMT1RR"
NEWS_API_KEY = "f241e24aaf25403aab3d94682d003ccf"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# Message about company and prices
NEWS_EXCHANGE = ""
# Twilio token and sid
account_sid = "ACd3b8a41006be0aadf5c843b73ed07f7e"
auth_token = "697cfa2e9863bbe1796f32cf33b2e10f"

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
responses = requests.get(STOCK_ENDPOINT, params=stock_params)
data = responses.json()
data_list = [value for value in data.values()]
# Get prices a few days before
before_yesterday_data = data_list[1]["2022-04-28"]
yesterday_data = data_list[1]["2022-04-29"]
pprint.pprint(before_yesterday_data)
pprint.pprint(yesterday_data)
# Get keys
before_yesterday_closing_price = float(before_yesterday_data["4. close"])
yesterday_closing_price = float(yesterday_data["4. close"])
try:
    print(
        f"New data from the last week - {abs(before_yesterday_closing_price - yesterday_closing_price)}"
    )
except IndexError as e:
    print(e)
# Convert data
difference = yesterday_closing_price - before_yesterday_closing_price
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(f"Difference between prises is: {abs(diff_percent)}\n")
# Check if vaues change than we waited also working with newsAPI
if diff_percent < 2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "sortBy": "relevancy",
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # pprint.pprint(articles)
    three_articles = articles[:3]
    # pprint.pprint(three_articles)
    for article in three_articles:
        main_articles = article["title"]
        main_descriptions = article["description"]
        NEWS_EXCHANGE += f"Headline: {main_articles}\nBrief: {main_descriptions}\n\n"


def send_message():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=NEWS_EXCHANGE,
        messaging_service_sid="MG8585a2717130cc456fca506d0504dc4d",
        to="+380966415756",
    )
    print(message.sid)


send_message()
