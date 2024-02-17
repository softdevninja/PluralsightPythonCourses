#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Pluralsight PythonPath console based Rock, Paper, & Scissor game. 
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

import random as rnd

computer_choice : str = 'default'
user_choice : str = 'default'

user_choice = input(f'{"Do you want rock, paper, or scissor?"}\n')

choices : list = ['rock','paper', 'scissor']
selection = rnd.randrange(0,3)
computer_choice = choices[selection]

if computer_choice == user_choice:
    print(f'{"TIE"}')
elif user_choice == 'rock' and computer_choice == 'scissor':
    print(f'{"YOU WIN"}')
elif user_choice == 'paper' and computer_choice == 'rock':
    print(f'{"YOU WIN"}')
elif user_choice == 'scissor' and computer_choice == 'paper':
    print(f'{"YOU WIN"}')
else:
    print(f'{"YOU LOSE"}')