import random

#Build using functions too.
#Build the guess function first
def guess():
    lives = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    print("I'm thinking of a number between 1 and 100.")
    if difficulty == "easy":
        lives = 9
    else:
        lives = 4
    print(f"You have {lives + 1} attempts to guess the number.")
    number = [random.choice(range(1, 101))] #Optionally use randint(1, 100)
    user_guess = int(input("Make a guess: "))

    #Define how the user will play
    start_game = True
    while start_game and lives > 0:
        if user_guess == number[0] and lives > 0:
            print("You guessed the number. You win!")
            start_game = False

        if user_guess != number and lives > 0:
            lives -= 1
        #Bugs: Was not setting the new guess to user_guess
            if user_guess > number[0]:
                print("Too high.")
                print(f"You have {lives + 1} attempts remaining to guess the number.")
                user_guess = int(input("Guess again: "))

            elif user_guess < number[0]:
                print("Too low.")
                print(f"You have {lives + 1} attempts remaining to guess the number.")
                user_guess = int(input("Guess again: "))

        if lives == 0:
            print("You ran out of guesses. You lose.")
            print("The number was", number[0])
            start_game = False
            guess()
guess()