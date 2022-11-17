from turtle import Turtle
import random


class Ball:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 1
        self.width = 1
        self.ball = Turtle("circle")
        self.x_move = 10
        self.y_move = 1
        self.create()

    def create(self):
        self.ball.speed(1)
        self.ball.penup()
        self.ball.color("green")

    def move(self):
        self.x += self.x_move
        self.y += self.y_move
        self.ball.goto(self.x, self.y)

    def bounce_to_bottom(self):
        self.y_move *= -1

    def bounce_to_left(self):
        self.x_move *= -1
