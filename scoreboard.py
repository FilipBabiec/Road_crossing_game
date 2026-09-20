from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.pendown()
        self.write(f"Current level: {self.score}", font=("Arial",20,"normal"))

    def raise_level(self):
        self.score += 1
        self.clear()
        self.write(f"Current level: {self.score}", font=("Arial",20,"normal"))

    def end_game(self):
        exit()