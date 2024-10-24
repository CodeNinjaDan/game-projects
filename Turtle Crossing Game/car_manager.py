COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.goto(280, 0)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.move = STARTING_MOVE_DISTANCE
        self.color(COLORS[0])

    def move_cars(self):
        self.forward(self.move)
