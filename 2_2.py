import turtle
turtle.shape('turtle')


def draw_number(movements):
	turtle.pendown()
	for step, angle in movements:
		turtle.forward(step)
		turtle.left(angle)
def draw_space():
    turtle.penup()
    turtle.forward(100)
    
diagonal=50 * 2**(0.5)
number_0 = [(0, 270), (100, 270), (50, 270), (100, 270), (50,0)]
number_1 = [(0, 270), (100, 180), (100, 135), (diagonal, 180), (diagonal, 315)]
number_2 = [(50, 225), (diagonal, 45), (50, 90), (50, 90)]
number_3 = [(diagonal, 135), (50, 225), (diagonal, 135), (50, 180)]
number_4 = [(0, 270), (100, 180), (100, 180), (50, 270), (50, 270), (50, 180), (50, 90) , (50, 90), (50, 270)]
number_5 = [(50, 90), (50, 90), (50, 270), (50, 270), (50, 0)]
number_6 = [(50, 90), (50, 90), (50, 90), (50, 180), (50, 315), (diagonal, 225)]
number_7 = [(0, 180), (50, 180), (50, 225), (diagonal, 45), (50, 180), (50, 315), (diagonal, 315)]
number_8 = [(50, 90), (100, 90), (50, 90), (100, 180), (50, 270), (50, 270)]
number_9 = [(0, 45), (diagonal, 45), (50, 90), (50, 90), (50, 90), (50, 90)]


turtle.penup()
turtle.left(180)
turtle.forward(400)
turtle.left(180)
turtle.pendown

ind=(number_1, number_4, number_1, number_7, number_0, number_0)
for i in ind:
	draw_number(i)
	draw_space()
