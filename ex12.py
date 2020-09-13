import numpy as np
import turtle
turtle.shape('turtle')

def circlearc(angle,radius):
    for i in range (int(angle/3)):
            turtle.right(3)
            turtle.forward(2*np.pi*radius/120)
            
turtle.left(90)	
number=int(input('Введите количество витков пружины'))
for i in range(number):
	circlearc(180,60)
	circlearc(180,10)
	
