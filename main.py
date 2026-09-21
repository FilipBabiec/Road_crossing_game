import time
from turtle import Screen

import scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
score = Scoreboard()
cars = CarManager()
screen.listen()

screen.onkey(key="Up", fun=tim.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.spawn_car()
    cars.move_cars(score, tim, screen)
    tim.check_for_win(score)
    screen.update()
