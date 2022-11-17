from turtle import Turtle
import random


class Ball:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 1
        self.width = 1
        self.ball = Turtle("circle")
        self.create()

    def create(self):
        self.ball.speed(1)
        self.ball.penup()
        self.ball.color("green")

    def random_move(self):
        # random_x = random.randint(-400, 400)
        random_y = random.randint(-300, 300)
        self.ball.goto(320, random_y)




