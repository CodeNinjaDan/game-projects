print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[ Dan ]
*******************************************************************************

''')

print("Welcome to treasure island.")
print("Your mission is to find the treasure.")
direction = input("Where do you want to go, left or right? \n").lower()

if direction == "right" :
    print("Dead End. Game over! :(")

elif direction == "left":
    choice = input("Would you like to swim or wait? \n").lower()

    if choice == "swim":
        print("You got bit by a Shark! Sorry:(")

    elif choice == "wait":
        door = input("Which door would you like to take: Blue, Red or Pink? \n").lower()

        if door == "blue":
            print("You walked into a booby trap. You Lose! :(")

        elif door == "red":
            print("False door. You Lose! :(")

        elif door == "pink":
            print("You win! Congratulations!")

        else:
            print("Door doesn't exist! Game over!")

    else:
        print("Invalid input. Game over!")

else:
    print("Invalid input. Game Over!")
