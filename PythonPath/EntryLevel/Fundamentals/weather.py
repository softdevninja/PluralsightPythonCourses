#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Pluralsight PythonPath weather API Request from example. 
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

from dotenv import load_dotenv
import requests
import os

load_dotenv('.env')
api_key: str = os.getenv('API_KEY')
location: str = "Clearwater"

url = 'http://api.weatherapi.com/v1/current.json?key='+api_key+'&q='+location+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print(f'{api_key}')
#print(f'{weather_json}')
print(f'Today\'s weather in {location} is {description} and {temp} degrees')