import requests
import bs4
import sys

#WAKEWORD joke
def suchar():
    try:
        resp = requests.get('http://piszsuchary.pl/losuj')
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')

    suchar = soup.find_all('pre')[0].get_text()

    return suchar[:suchar.find('|')]

