import webbrowser
import requests
import json

def show_the_weather(city=''):
    webbrowser.open('https://www.google.com/search?q=pogoda {}'.format(city))

def get_the_weather(city, api_key):
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q={},pl&APPID={}'.format(city, api_key))
    json_data = json.loads(resp.text)
    print('{desc}, temperature is currently {temp} Celcius degrees, wind speed {wind} m/s'.format(desc=json_data['weather'][0]['main'], temp=(json_data['main']['temp'] - 273.15)*10//1/10, wind=json_data['wind']['speed']))