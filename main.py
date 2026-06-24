import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(key="Up", fun=player.move_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.spawn_car()
    car_manager.move_cars()

    if player.has_crossed_finish_line():
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_speed()

    if car_manager.car_collision(player):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
