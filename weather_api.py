import requests
import settings


class OpenWeather:
    BASE_URL = f'https://api.openweathermap.org/data/2.5/weather?lang={settings.LANGUAGE}'

    def __init__(self, key=''):
        self.key = key

    def get_weather(self, city_name):
        response = requests.get(f'{self.BASE_URL}&q={city_name}&appid={self.key}')
        data = response.json()
        if data['cod'] == '404':
            raise Exception(f"Город с названием {city_name} не существует")

        description = data['weather'][0]['description']
        temp = data['main']['temp'] - 273.15
        feels_like = data['main']['feels_like'] - 273.15

        return {
            'description': description,
            'temp': temp,
            'feels_like': feels_like
        }

