#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""
Pluralsight PythonPath contacts from example. 
"""
__version__ = "1.0.0"
__author__ = "Doug Zuniga"
__email__ = "softdevninja@gmail.com"

contacts = {
    'number': 4,
    'students':
        [
            {'name':'Sarah Holderness', 'email':'sarach@example.com'},
            {'name':'Harry Potter', 'email':'harry@example.com'},
            {'name':'Hermoione Granger', 'email':'hermione@example.com'},
            {'name':'Ron Weasley', 'email':'ron@example.com'},
        ]
}

print(f'Students emails:')
for student in contacts['students']:
    print(student['email'])