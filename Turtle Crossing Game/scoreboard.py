FONT = ("Courier", 30, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(self.score, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def increase_level(self):
        pass
