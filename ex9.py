import numpy
import turtle
turtle.shape('turtle')

def polygon(n,side):
	angle=180*(n-2)/n
	turtle.left(180-angle/2)
	for i in range(n):
		turtle.forward(side)
		turtle.left(180-angle)
	turtle.right(180-angle/2)
	
number=int(input('Введите количество многоугольников'))
r=40;
for i in range(number):
	turtle.penup()
	turtle.forward(r)
	turtle.pendown()
	polygon(i+3,2*r*numpy.sin(numpy.pi/(i+3)))
	turtle.penup()
	turtle.backward(r)
	r+=15;

	   
