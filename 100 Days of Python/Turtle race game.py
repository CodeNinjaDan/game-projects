from turtle import  Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle do you think will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]

#Learn to use outputs of functions as inputs of other functions.
#Like in "y=y_positions[turtle_index]" and in "colors[turtle_index]" took the outputs(current number in the loop)
#and used them as inputs to get the y_position and and the color for each turtle
#which is easier than using variables and changing them at each loop
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

#Prevent the race from starting if the user has not yet entered their guess
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won. {winning_color} won the race!")
            else:
                print(f"You lost. {winning_color} won the race!")

        race_pace = random.randint(1, 10)
        turtle.forward(race_pace)

screen.exitonclick()