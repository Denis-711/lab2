import turtle
turtle.shape('turtle')

from random import *

turtle.speed(2)
for i in range(1000):
	turtle.forward(randint(0,50))
	turtle.left(randint(-180,180))
