import numpy as np;
import turtle
turtle.shape('turtle')


def circlearc(angle,radius):
    turtle.penup()
    turtle.forward(radius)
    turtle.pendown()
    turtle.right(90)
    for i in range (int(angle/3)):
        turtle.right(3)
        turtle.forward(2 * np.pi * radius / 120)
    turtle.penup()
    turtle.left(90)    
    turtle.backward(radius)
def circle(radius,color):
    turtle.penup()
    turtle.forward(radius)
    turtle.color('black',color)
    turtle.pendown()
    turtle.right(90)
    turtle.begin_fill()
    for i in range (int(360/3)):
        turtle.right(3)
        turtle.forward(2 * np.pi * radius / 120)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)    
    turtle.backward(radius)
	
    
#лицо
circle(100,'yellow')

#глаза
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(25)
circle(15,'blue')
turtle.backward(50)
circle(15,'blue')

#нос
turtle.width(10)
turtle.forward(25)
turtle.right(90)
turtle.forward(30)
turtle.pendown()
turtle.forward(40)
turtle.penup()

#рот
turtle.forward(20)
turtle.left(90)
turtle.color('red','red')
circlearc(180,50)
