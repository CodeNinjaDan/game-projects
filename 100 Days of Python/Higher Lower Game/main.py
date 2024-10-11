import random
from game_data import data
from art import logo, vs
#1. Art
#2. Function -> Randomly choose characters from dict inside a list in game_data
#       -> Display the chosen characters as A and B
#       -> If pick_a and pick_b are the same, place them in a while loop to pick again
#3. Display for the user to pick who has more followers
#   -> When displaying, show the person's name, what they do and where they're from(Retrieve from the nested dictionary)
#4. Win function -> If the user_guess == random choice :
#       then B moves to a and the next person to guess is displayed
#       the game goes on until the user loses.
#
# pick_a = random.choice(data)
# follower_values_a = pick_a['follower_count']
# print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")
#
# pick_b = random.choice(data)
# while pick_b == pick_a:
#     pick_b = random.choice(data)
# follower_values_b = pick_b['follower_count']
# print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}")

def guess():
    pick_a = random.choice(data)
    follower_values_a = pick_a['follower_count']
    print(logo)
    print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")
    print(vs)
    pick_b = random.choice(data)
    while pick_b == pick_a:
        pick_b = random.choice(data)
    follower_values_b = pick_b['follower_count']
    print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}")
    score = 0
    start_game = True

    while start_game:
        user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_answer == "A" and follower_values_a > follower_values_b:
            pick_a = pick_b
            follower_values_a = follower_values_b
            pick_b = random.choice(data)
            while pick_b == pick_a:
                pick_b = random.choice(data)
            follower_values_b = pick_b['follower_count']
            score += 1
            print(f"You're right! Current score: {score}")
            print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")
            print(vs)
            print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}")

        elif user_answer == "B" and follower_values_b > follower_values_a:
            pick_a = pick_b
            follower_values_a = follower_values_b
            pick_b = random.choice(data)
            while pick_b == pick_a:
                pick_b = random.choice(data)
            follower_values_b = pick_b['follower_count']
            score += 1
            print(f"You're right! Current score: {score}")
            print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")
            print(vs)
            print(f"Against B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}")

        else:
            print(f"Sorry, that's wrong. Your final score is: {score}")
            start_game = False

guess()

#********************************************           OR           ***************************************************
def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
# Generate a random account from the game data
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
