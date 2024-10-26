from turtle import Turtle


#Use constants for easy code editing
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        with open("data.txt") as file:
            number = int(file.read())

        self.score = 0
        self.high_score = number
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.update_scoreboard()

    #Create functions to reduce repetition.
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
            with open("data.txt", mode="w") as high:
                high.write(self.high_score)

        self.score = 0
        self.update_scoreboard()



    def track_score(self):
        self.score += 1
        self.update_scoreboard()
