from turtle import Turtle

INITIAL_POSITION1 = [(300, -40), (300, -20), (300, 0), (300, 20), (300, 40)]
INITIAL_POSITION2 = [(-300, -40), (-300, -20), (-300, 0), (-300, 20), (-300, 40)]


class Paddle:
	def __init__(self,):
		self.width = 1
		self.height = 1


	def create_Player1_Paddle(self):
		self.create_paddle(INITIAL_POSITION1)

	def create_Player2_Paddle(self):
		self.create_paddle(INITIAL_POSITION2)

	def create_paddle(self,  initial_position):
		for position in initial_position:
			paddle_component = Turtle("square")
			paddle_component.color("white")
			paddle_component.shapesize(self.width, self.height)
			paddle_component.penup()
			paddle_component.goto(position)
