import random

print('Welcome to your password generator')

chars = 'QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm,./1234567890@#$%&'

number = input('Amount of passwords to generate:')
number = int(number)

length = input('Number of characters in each password:')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
