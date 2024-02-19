#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Pluralsight PythonPath loan calculator from example. 
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

# Loan details
money_owed = float(input('How much money do you owe, in dollars?\n')) 
apr = float(input('What is the annual percentage rate of the loan?\n'))
payment = float(input('How much will you pay off each month in dollars?\n'))
months = int(input('How many months do you want to see the results for?\n'))

monthly_rate = (apr/100) / 12

for i in range(months):

    # Calculate interest to pay
    interest_paid = money_owed * monthly_rate

    # Add in interest
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print(f'The last payment is {money_owed:.2f}')
        print(f'You paid off the loan in {i + 1} months')
        break

    # Made payment
    money_owed = money_owed - payment

    print(f'paid {payment:.2f} of which {interest_paid:.2f} was interest', end=' ')
    print(f'Now I owe {money_owed:.2f}')