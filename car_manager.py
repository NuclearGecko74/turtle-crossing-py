from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT_PERCENTAGE = 0.2


def generate_car():
    new_car = Turtle("square")
    new_car.penup()
    new_car.color(choice(COLORS))
    new_car.shapesize(stretch_wid=1, stretch_len=2)
    return new_car

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        if self.cars and self.cars[-1].xcor() >= 260:
            return
        for _ in range(randint(1, 2)):
            car = generate_car()
            car.goto(300, randint(-200, 260))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars[:]:
            car.backward(self.move_distance)

            if car.xcor() < -300:
                self.cars.remove(car)
                car.hideturtle()

    def increase_speed(self):
        self.move_distance *= 1 + MOVE_INCREMENT_PERCENTAGE

    def car_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 25 and player.ycor() < car.ycor():
                return True
        return False
