#!/usr/bin/python3
import string
import random

print('')
print('HEX PASSWORD GENERATOR')
print('')

length = input('HOW LONG: ')
length = int(length)

qty = input('HOW MANY: ')
qty = int(qty)


for y in range(qty):
    password = ''
    for c in range(length):
        password += random.choice(string.hexdigits)
    print(password)
