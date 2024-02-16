#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Pluralsight PythonPath age/decades calculator.
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"


age : int = 0
age = int(input(f'How old are you?\n'))
decades : int  = age // 10

print(f'{"You are " + str(decades) + " decades and " + str(age) + " old."}')