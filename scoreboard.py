from turtle import Turtle
from tkinter import messagebox

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-290, 260)
        self.pendown()
        with open("high_score.txt") as file:
            self.highscore = int(file.read())
        self.update_scoreboard()

    def raise_level(self):
        self.score += 1
        self.update_scoreboard()

    def end_game(self, screen):
        screen.update()
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as f:
                f.write(str(self.highscore))

            messagebox.showinfo(
                title="Game over",
                message=f"You got hit!\n\nYou have hit a new high score!\n\nLevel reached: {self.score}",
                parent=screen.getcanvas().winfo_toplevel(),
            )
            self.score = 0
            screen.bye()

        else:
            messagebox.showinfo(
                title="Game over",
                message=f"You got hit!\n\nLevel reached: {self.score}",
                parent=screen.getcanvas().winfo_toplevel(),
            )
            self.score = 0
            screen.bye()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Current level: {self.score}    High score: {self.highscore}", font=FONT)