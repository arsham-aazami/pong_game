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
	time.sleep(0.01)
	screen.update()

	pong_ball.move()

	# Detecting collision with wall
	if pong_ball.ball.ycor() == 280 or pong_ball.ball.ycor() == -280:
		# bounce the ball(up and down)
		pong_ball.bounce_to_bottom()
		print("a")
	if pong_ball.ball.xcor() == 380 or pong_ball.ball.xcor() == -380:
		paddle_x = player1_paddle.paddle_component.xcor()
		paddle_y = player1_paddle.paddle_component.ycor()

		dis_from_center = pong_ball.ball.distance(paddle_x, paddle_y)
		dis_from_top = pong_ball.ball.distance(paddle_x + 5, paddle_y + 5)
		dis_from_bottom = pong_ball.ball.distance(paddle_x - 5, paddle_y - 5)
		if dis_from_center < 50 or dis_from_top < 90 or dis_from_bottom < 90:
			pong_ball.bounce_to_left()
		else:
			is_game_ended = True
			game_over()
			print("b")

screen.mainloop()
