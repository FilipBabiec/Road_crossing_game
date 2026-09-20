from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.carlist = []


    def spawn_car(self):
        car = Turtle("turtle")
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(270)
        car.goto(320, random.randint(-270, 270))
        self.carlist.append(car)

    def move_cars(self, level):
        for car in self.carlist:
            car.forward(STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)