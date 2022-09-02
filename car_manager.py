from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.setposition(280, random.randint(-250, 250))
            new_car.setheading(180)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            self.cars.append(new_car)

    def auto_move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        global  STARTING_MOVE_DISTANCE,MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
