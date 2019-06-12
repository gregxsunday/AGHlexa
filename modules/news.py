import requests
import json

#WAKEWORD news @topic
def news(topic):
    with open("D:\Docs\studia\semestr 4\python\\newskey.txt", 'r') as infile:
        api_key = infile.read()
    url = f'https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en'
    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return 'News not found'
    resp = json.loads(resp.text)
    try:
        news = resp['articles'][0]['description']
        return news
    except Exception as e:
        return 'News not found'