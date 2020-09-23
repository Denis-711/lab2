from random import randint
import turtle 


number_of_turtles = 20

#drawing container
turtle.width(10)
turtle.penup()
turtle.goto(-300, - 300)
turtle.pendown()
turtle.goto(-300, 300)
turtle.goto(300, 300)
turtle.goto(300, -300)
turtle.goto(-300, -300)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
	unit.penup()
	unit.goto(randint(-300, 300), randint(-300, 300))
	unit.seth(randint(-180, 180))


#moving moleculs
for i in range(1000):
	for unit in pool:
		if abs(unit.xcor()) > 300:
			unit.seth(180-unit.heading())
		if abs(unit.ycor()) > 300:
			unit.seth(360-unit.heading())
		unit.forward(unit.speed())
