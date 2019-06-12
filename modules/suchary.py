import requests
import bs4

#WAKEWORD joke
def suchar():
    try:
        resp = requests.get('http://piszsuchary.pl/losuj')
    except requests.exceptions.RequestException as e:
        print(e)
        return 'Joke not found'
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')

    try:
        suchar = soup.find_all('pre')[0].get_text()
    except Exception as e:
        print(e)
        return 'Joke not found'

    return suchar[:suchar.find('|')]

