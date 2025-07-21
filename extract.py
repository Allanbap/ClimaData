import requests

def get_weather_data(url):
    response = requests.get(url)
    return response.json()