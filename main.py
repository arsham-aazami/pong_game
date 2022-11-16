from turtle import Turtle, Screen
from paddlle import Paddle


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("#000000")
screen.tracer(1)
screen.title("Pong")

# Implementing paddles
player1_paddle = Paddle(300, 0)
player1_paddle.createPaddle()

player2_paddle = Paddle(-300, 0)
player2_paddle.createPaddle()

# Implementing the middle line
for y_position in range(-300, 300, 20):
	square = Turtle("square")
	square.shapesize(0.4, 0.4)
	square.speed(0)
	square.color("white")
	square.penup()
	square.goto(0, y_position)



screen.mainloop()

