import requests
import json

url = "https://newsapi.org/v2/top-headlines/sources?country=us&apiKey=2a644345d7834938ba86a705c41c378c"

response = requests.get(url)
data = response.json()
