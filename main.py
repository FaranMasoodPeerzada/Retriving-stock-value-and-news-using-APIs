import requests
from twilio.rest import Client
stock_api_key="X2JB11EA4V6XWKAP"
news_api_key="6c71af678eea4df79ad39be4feb9ad26"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = "AC5559bb4f8d344bbdcf4652e867dad124"
auth_token = "aec3da226a0d252040af773056a8dfe8"

stock_parameter={"function":'TIME_SERIES_DAILY_ADJUSTED',
                 "symbol":STOCK,
                 "apikey":stock_api_key}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
response= requests.get(STOCK_ENDPOINT,params=stock_parameter)
response.raise_for_status()
data= response.json()
final_data=data['Time Series (Daily)']
data_list= [value for (key, value) in final_data.items()]
yesterday=data_list[0]['4. close']

print("+++")
before_yesterday=data_list[1]['4. close']
print(yesterday)
difference=abs(float(yesterday)-float(before_yesterday))
difference_percent=(difference/float(yesterday))*100
print(difference)
print(difference_percent)
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if difference>3:
  
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.


    news_parameter={"qInTitle":COMPANY_NAME,
        "apiKey":news_api_key,
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_parameter)
    news_response.raise_for_status()
    news_data=news_response.json()
    top_news=news_data['articles'][0:3]
    for news in top_news:
        client = Client(account_sid, auth_token)
        message = client.messages \
        .create(
        body=f"TSLA: 🔺{difference}%\n\nHeadline:{news['title']}\n\n Brief: {news['description']}",
        from_='+15075007052',
        to='+923005078036'
         )

