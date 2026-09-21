from turtle import Turtle
from tkinter import messagebox

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

    def end_game(self, screen):
        screen.update()  # draw the final frame so the collision is visible behind the popup
        messagebox.showinfo(
            title="Game over",
            message=f"You got hit!\n\nLevel reached: {self.score}",
            parent=screen.getcanvas().winfo_toplevel(),
        )
        screen.bye()  # close the game window after OK