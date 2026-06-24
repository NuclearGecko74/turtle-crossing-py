from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.setup_scoreboard()
        self.update_scoreboard()

    def setup_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-290, 260)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
