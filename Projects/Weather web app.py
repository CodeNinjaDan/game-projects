
import requests
from pprint import pprint

API_Key = '30f2b1d21c55231cdaaef7d9dabe0726'

city = input('Enter a city: ')

base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}'


weather_data = requests.get(base_url)

if weather_data.status_code == 200:
    weather = weather_data.json()
    pprint(weather)
else:
    print('Error: Could not retrieve data')
