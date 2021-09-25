from newsapi import NewsApiClient
import json

# クライアントを初期化
newsapi = NewsApiClient(api_key='2a644345d7834938ba86a705c41c378c')

# qと国で記事全体を取得
response = newsapi.get_everything(q='bitcoin', language='en')
#headlines = newsapi.get_top_headlines(category='business', country='us')

#この間でJSON データをスライスしたい。

for response_key in response:
    print(response_key)

'''def extract_data(response):
    for key in response['response'].keys():
        if not key.isdigit():
            continue
        d = response[articles][description][publishedAt]
        print(d)
'''

# print AllArticles
'''if (response['totalResults']>0):
    print(response['articles'][0:9])
else:
    print('No News are found')'''

# 取得したトップニュースの１件を表示 print(headlines['articles'][0])