#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Pluralsight PythonPath movie schedule from example. 
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

current_movies = {'The Grinch': '10:00am',
                  'Rudolph': '1:00pm',
                  'Frosty the Snowman': '3:00pm',
                  'Christmas Vacation': '5:00pm'}

print(f'We\'re showing the following movies:')

for key in current_movies:
    print(f'{key}')

movie = input(f'Which movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print(f'Requested movie isn\'t playing')
else:
    print(f'{movie} is playing at {showtime}')      