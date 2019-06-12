import requests
import json

class Weather:
    def __init__(self, city, api_key):
        self.error = ''
        try:
            resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(city, api_key))
        except requests.exceptions.RequestException as e:
            self.error = 'Weather not found'

        json_data = json.loads(resp.text)
        self.extract(json_data)

    def extract(self, json_data):
        try:
            self.desc = json_data['weather'][0]['main']
            self.temp = (json_data['main']['temp'] - 273.15) * 10 // 1 / 10
            self.wind = json_data['wind']['speed']
        except KeyError as e:
            self.error = 'Weather not found'

    def print_weather(self):
        print('{desc}, temperature is currently {temp} Celcius degrees, wind speed {wind} m/s'.format(
            desc=self.desc, temp=self.temp,
            wind=self.wind))

    def get_weather(self):
        return '{desc}, temperature is currently {temp} Celcius degrees, wind speed {wind} m/s'.format(
            desc=self.desc, temp=self.temp,
            wind=self.wind)

# #WAKEWORD weather @CITY
# def show_the_weather(city=''):
#     webbrowser.open('https://www.google.com/search?q=pogoda {}'.format(city))


# WAKEWORD weather @city
def print_the_weather(city):
    with open("D:\Docs\studia\semestr 4\python\openweatherkey.txt", 'r') as infile:
        api_key = infile.read()
    weather = Weather(city, api_key)
    if weather.error != '':
        return weather.error
    return weather.get_weather()