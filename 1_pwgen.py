#!/usr/bin/python3

print('')
print('HEX PASSWORD GENERATOR')
print('')

import random
import string


print('-' * 30)
length = input('Length: ')
length = int(length)
print('-' * 30)
qty = input('Quantity: ')
qty = int(qty)
print('-' * 30)
print('Types of passowrds I can create...')
print('hex = abcdefABCDEF1234567890')
print('alpha = a-z,A-Z')
type = input('Type: ')

while True:
        if type.startswith('h'):
            for c in range(length):
                password += random.choice(string.hexdigits)
            print(password)
            break
        elif type.startswith('a'):
            for c in range(length):
                password += random.choice(string.ascii_letters)
            print(password)
            break
        
