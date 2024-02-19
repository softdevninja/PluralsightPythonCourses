#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Pluralsight PythonPath space_people API Request from example. 
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

print(f'{json}')

print(f'The people currently in space are:')
for p in json['people']:
    print(f'{p["name"]}')