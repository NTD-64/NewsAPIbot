from newsapi import NewsApiClient
import json

# クライアントを初期化
newsapi = NewsApiClient(api_key='2a644345d7834938ba86a705c41c378c')

# qと国で記事全体を取得
AllArticles = newsapi.get_everything(q='crypt', country='us')

if (AllArticles['totalResults'] > 0):
    print(AllArticles['articles'][0:9])
else:
    print('No News are found')

# 取得したトップニュースの１件を表示 print(headlines['articles'][0])
