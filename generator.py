
# This is just a password generator.

import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

number = input('Number of passwords: ')
number = int(number)

length = input('Password length: ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)

# This line is just to make the file not close after if finishes the tasks.
xyz = input()
