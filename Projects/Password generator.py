import random

print('Welcome to your password generator')

chars = 'QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm,./1234567890@#$%&'

number = int(input('Amount of passwords to generate:'))

length = int(input('Number of characters in each password:'))


print('\nhere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
