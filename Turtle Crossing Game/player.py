STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setposition(STARTING_POSITION)
        self.color("limegreen")
        self.setheading(90)
        self.move = MOVE_DISTANCE


    def move_up(self):
        self.forward(self.move)