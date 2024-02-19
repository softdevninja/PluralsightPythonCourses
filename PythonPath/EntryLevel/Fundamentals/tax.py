#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Pluralsight PythonPath simple tax calculator from example.
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

amount : int = 10
tax : float = 0.06
total : float = amount + amount  * tax

print(f'{total}')