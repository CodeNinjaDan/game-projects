
import requests
from pprint import pprint

API_Key = ' ' # Enter your API key here

city = input('Enter a city: ')

base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}'


weather_data = requests.get(base_url)

if weather_data.status_code == 200:
    weather = weather_data.json()
    pprint(weather)
else:
    print('Error: Could not retrieve data')
