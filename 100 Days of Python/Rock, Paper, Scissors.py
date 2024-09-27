import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user = input("What is your choice, 'r' for 'rock', 'p' for 'paper' or 's' for 'scissors'? \n" ).lower()
if user == 'r':
    print(rock)
elif user == 'p':
    print(paper)
elif user == 's':
    print(scissors)
else:
    print("Not a valid choice. Try again!")

computer = random.choice(['r', 'p', 's'])
print(f"Computer chose: {computer}")
if computer == 'r':
    print(rock)
elif computer == 'p':
    print(paper)
else:
    print(scissors)


if user == computer:
    print("It's a draw!")

elif computer == 'r' and user == 'p':
    print("You win!:(")

elif computer == 'p' and user == 's':
    print("You win!:(")

elif computer == 's' and user == 'r':
    print("You win!:)")

elif user == 'r' and computer == 'p':
    print("You lose!:(")

elif user == 'p' and computer == 's':
    print("You lose!:(")

elif user == 's' and computer == 'r':
    print("You lose!:(")
