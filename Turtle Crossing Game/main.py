import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Race Game.")
screen.tracer(0)
player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

loop = 0

game_is_on = True
while game_is_on:
    car.move_cars()
    time.sleep(0.1)
    screen.update()

    loop += 1
    if loop % 6 == 0:
        car.generate_car()
        car.move_cars()


    #Detect collision between turtle and car.
    for car_instance in car.all_cars:
        if player.distance(car_instance) < 25:
            game_is_on = False

    if player.ycor() > 280:
        player.goto(STARTING_POSITION)
        car.increase_speed()
        score.increase_score()

screen.exitonclick()