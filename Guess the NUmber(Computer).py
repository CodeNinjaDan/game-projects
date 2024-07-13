# Computer generates a random number to be guessed by a user
import random

def guess(y):
    random_number = random.randint(1, y)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {y}: '))
        if guess < random_number:
            print('Too low. Guess again.')
        elif guess > random_number:
            print('Too high. Guess again.')
    print(f'Congratulations! You got the number {random_number} correct!')

guess(10)
    
        
