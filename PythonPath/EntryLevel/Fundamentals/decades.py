#!/usr/bin/env python3

age : int = 0
age = int(input(f'How old are you?\n'))
decades : int  = age // 10

print(f'{"You are " + str(decades) + " decades and " + str(age) + " old."}')