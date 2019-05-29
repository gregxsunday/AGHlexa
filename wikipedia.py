import requests
import bs4
import re
import json
import sys

def remove_brackets(text):
    while text.find('(') != -1:

        start = text.find('(')
        end = text.find(')')
        if start != -1 and end != -1:
            text = text[:start] + text[end + 1:]
    return text


#WAKEWORD wikipedia @query
def find_on_wikipedia(query):
    try:
        resp = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search={}&namespace=0&limit=10&suggest=true'.format(query))
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    res = json.loads(resp.text)
    urls = res[3]

    if len(urls) == 0:
        return 'Not found'
    else:
        url = urls[0]

    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    ps = soup.find_all('p')
    paragraph = ps[2].get_text()
    first_sentence = paragraph[:paragraph.find('.', len(query)) + 1]
    first_sentence = remove_brackets(first_sentence)
    return first_sentence

