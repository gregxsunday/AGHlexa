import webbrowser
import requests
import json

class Weather:
    def __init__(self, city, api_key):
        try:
            resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q={},pl&APPID={}'.format(city, api_key))
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        json_data = json.loads(resp.text)
        self.extract(json_data)

    def extract(self, json_data):
        self.desc = json_data['weather'][0]['main']
        self.temp = (json_data['main']['temp'] - 273.15) * 10 // 1 / 10
        self.wind = json_data['wind']['speed']

    def print_weather(self):
        print('{desc}, temperature is currently {temp} Celcius degrees, wind speed {wind} m/s'.format(
            desc=self.desc, temp=self.temp,
            wind=self.wind))

#WAKEWORD show me the weather in @CITY
def show_the_weather(city=''):
    webbrowser.open('https://www.google.com/search?q=pogoda {}'.format(city))

#WAKEWORD what is the weather in @city
def print_the_weather(city, api_key):
    weather = Weather(city, api_key)
    weather.print_weather()