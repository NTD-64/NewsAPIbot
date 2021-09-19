import json
import requests

def fetch_data(**params):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=2a644345d7834938ba86a705c41c378c'
    response = requests.get(url,params)
    return response.json()

def extract_data(response):
    for key in responce['response'].keys():
        if not key.isdigit():
            continue
        d = response['response'][key]['photo']
        if d.get('comment') and d.get('total_score'):
            comment =d['comment']
            score = d['total_score']
            data = {
                'comment': comment
                'score': score
            }
            yield data
def save_as_json(save_file,record):
    with open(save_file, mode='a') as f:
        f.write(json.dumps(record) + '/n')

def main():
    #set fixed names
    raw_data = 'data/raw_data.json'
    save_file ='data/raw_data.jsonl'
    keyid ='YOUR API ID'

    response = fetch_data(
        keyid = keyid,
        area =
        hit_per_page = 50
    )
