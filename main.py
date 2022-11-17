from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
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

# Implementing Game over text

def game_over():
    text = Turtle()
    text.color("white")
    text.write("Game Over", align="center", font=("Arial", 8, "normal"))
    text.hideturtle()


is_game_ended = False
while not is_game_ended:
    time.sleep(0.1)
    screen.update()
    # if pong_ball.ball.distance():
    pong_ball.random_move()
    if pong_ball.ball.xcor() == 400:
        is_game_ended = True
        game_over()
screen.mainloop()
