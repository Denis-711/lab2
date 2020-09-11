import turtle
import numpy as np

def circle(r):

    for i in range (72):
        turtle.left(5)
        turtle.forward(2*np.pi*r/72)
n=int(input())
turtle.shape('turtle')
radius=40
turtle.left(90)
for i in range (n):
    
    circle(radius)
    turtle.left(180)
    circle(radius)
    radius+=5;
