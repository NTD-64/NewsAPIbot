import requests
import json

url = ('https://newsapi.org/v2/top-headlines/sources?country=us&apiKey=2a644345d7834938ba86a705c41c378c')

#var = ('http://newsapi.org/v2/top-headlines?'
 #      'q=trump&'  # the keyword we are looking for
  #     'country=us&'  # we chose the country we want
   #    'category=general&'  # we chose the category we want
    #   'language=en&'  # we chose the language we want
     #  'pageSize=30&'  # no. of results. Default 20, max 100
      # 'apiKey=Your_api_key')  # Your Api keys

response = requests.get(url)
data = response.json()

print(json.dumps(data, sort_keys=True, indent=4))
