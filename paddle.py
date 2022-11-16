from turtle import Turtle


class Paddle:
	def __init__(self, x):
		self.paddle_component = None
		self.width = 10
		self.height = 2
		self.x = x
		self.y = 0
		self.step = 40

	def create_paddle(self):
		self.paddle_component = Turtle("square")
		self.paddle_component.speed(0)
		self.paddle_component.color("white")
		self.paddle_component.shapesize(self.width, self.height)
		self.paddle_component.penup()
		self.paddle_component.goto(self.x, 0)

	def move_up(self):
		if self.y < 200:
			self.y += self.step
			self.paddle_component.goto(self.x, self.y)

	def move_down(self):
		if self.y > -200:
			self.y -= self.step
			self.paddle_component.goto(self.x, self.y)
