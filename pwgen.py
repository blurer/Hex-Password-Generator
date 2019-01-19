#!/usr/bin/python3

print('')
print('HEX PASSWORD GENERATOR')
print('')

import random

chars = 'abcdefABCDEF1234567890'

length = input('HOW LONG: ')
length = int(length)

qty = input('HOW MANY: ')
qty = int(qty)


for y in range(qty):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
