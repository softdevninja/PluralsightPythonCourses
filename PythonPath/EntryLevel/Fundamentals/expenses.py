#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Pluralsight PythonPath expenses calculator from example. 
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

expenses : list = [10.50, 8, 5, 15, 20, 5, 3]
total_sum : float = 0.0

total_sum = sum(expenses)
    
print(f'{"You spent, $" + str(total_sum)}')