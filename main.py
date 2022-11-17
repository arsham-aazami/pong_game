from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("#000000")
screen.tracer(1)
screen.title("Pong")

# Implementing paddles
player1_paddle = Paddle(350)
player1_paddle.create_paddle()

player2_paddle = Paddle(-350)
player2_paddle.create_paddle()

# Adding event listeners
screen.listen()
screen.onkey(fun=player1_paddle.move_up, key="Up")
screen.onkey(fun=player1_paddle.move_down, key="Down")

# Implementing ball physics
pong_ball = Ball()
pong_ball.random_move()
if pong_ball.ball.distance(player1_paddle) < 10:
	print("1")
# Implementing the middle line
for y_position in range(-300, 300, 20):
	square = Turtle("square")
	square.shapesize(0.4, 0.4)
	square.speed(0)
	square.color("white")
	square.penup()
	square.goto(0, y_position)

screen.mainloop()
