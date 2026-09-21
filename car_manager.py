from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def check_collision(player, car, score, screen):
    if player.distance(car.xcor(),car.ycor()) < 20:
        score.end_game(screen)


class CarManager:
    def __init__(self):
        self.carlist = []


    def spawn_car(self):
        if random.randint(1,10) == 1:
            car = Turtle("turtle")
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(320, random.randint(-270, 270))
            self.carlist.append(car)

    def move_cars(self, score, player, screen):
        for car in self.carlist:
            car.forward(STARTING_MOVE_DISTANCE + score.score * MOVE_INCREMENT)
            check_collision(player, car, score, screen)
            if car.xcor() == -320:
                car.hideturtle()
                self.carlist.remove(car)

