import os
from newsapi import NewsApiClient

# クライアントを初期化
newsapi = NewsApiClient(api_key='2a644345d7834938ba86a705c41c378c')

# sourcesで指定したニュースサイトからトップニュースを取得
headlines = newsapi.get_top_headlines(sources='techcrunch')

# 取得したトップニュースの１件を表示
print(headlines['articles'][0])
