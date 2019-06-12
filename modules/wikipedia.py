import requests
import bs4
import json


def remove_brackets(text):
    while text.find('(') != -1:
        start = text.find('(')
        end = text.find(')')
        if start != -1 and end != -1:
            text = text[:start] + text[end + 1:]
    return text


#WAKEWORD wikipedia @query
def find_on_wikipedia(query):
    error_phrase = 'Wikipedia article not found'
    try:
        resp = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&format=json&formatversion=2&search={}&namespace=0&limit=10&suggest=true'.format(query))
    except requests.exceptions.RequestException as e:
        print(e)
        return error_phrase

    res = json.loads(resp.text)
    urls = res[3]

    if len(urls) == 0:
        return error_phrase
    else:
        url = urls[0]

    try:
        resp = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return error_phrase

    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    ps = soup.find_all('p')
    paragraph = ps[2].get_text()
    first_sentence = paragraph[:paragraph.find('.', len(query)) + 1]
    first_sentence = remove_brackets(first_sentence)
    if len(first_sentence) > 0:
        return first_sentence
    else:
        return error_phrase

