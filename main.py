import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.auto_move()

    # if collide with car
    for carX in car.cars:
        if player.distance(carX) < 27:
            print("you lose collide with car")
            game_is_on = False
            score.game_over()

    # if you win
    if player.race_is_finish():
        car.speed_up()
        score.score_edit()



screen.exitonclick()
