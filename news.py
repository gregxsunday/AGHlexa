import requests
import json
import sys

#WAKEWORD news about @topic
def news(topic, api_key):
    url = f'https://newsapi.org/v2/everything?q={topic}&from=2019-04-26&sortBy=publishedAt&apiKey={api_key}&language=en'
    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    resp = json.loads(resp.text)
    try:
        news = resp['articles'][0]['description']
        return news
    except Exception as e:
        return 'News not found'