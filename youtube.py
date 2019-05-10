import requests
import bs4
import webbrowser

def search(command):
    resp = requests.get('https://www.youtube.com/results?search_query={}'.format(command))
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    for link in soup.find_all('a'):
        if '/watch?v=' in link.get('href') and link.string != None:
            print('Opening {}'.format(link.string))
            webbrowser.open('https://www.youtube.com{}'.format(link.get('href')))
            return

