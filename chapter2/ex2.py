import turtle
turtle.shape('turtle')

def draw_number(movements):
	turtle.pendown()
	for step, angle in movements:
		turtle.forward(step)
		turtle.left(angle)
		
def move_to_next_cell():
    turtle.penup()
    turtle.forward(100)

#information for function draw_number how to draw a certain number  
diagonal = 50 * 2**(0.5)
number_0 = [(0, 270), (100, 270), (50, 270), (100, 270), (50,0)]
number_1 = [(0, 270), (100, 180), (100, 135), (diagonal, 180), (diagonal, 315)]
number_2 = [(0, 180), (50, 180), (50, 270), (50, 315), (diagonal, 135), (50, 180), (50, 225), (diagonal, 45), (50, 270)]
number_3 = [(0, 180), (50,180), (50, 225), (diagonal, 135), (50, 225), (diagonal, 180), (diagonal, 135), (50, 225), (diagonal, 315)]
number_4 = [(0, 270), (100, 180), (100, 180), (50, 270), (50, 270), (50, 180), (50, 90) , (50, 90), (50, 270)]
number_5 = [(0, 180), (50, 90), (50, 90), (50, 270), (50, 270), (50, 180), (50, 90), (50, 90), (50, 270), (50, 270), (50, 0)]
number_6 = [(0, 225), (diagonal, 135), (50,270), (50, 270), (50, 270), (50, 315), (diagonal, 315)]
number_7 = [(0, 180), (50, 180), (50, 225), (diagonal, 45), (50, 180), (50, 315), (diagonal, 315)]
number_8 = [(0, 180), (50, 180), (50, 270), (100, 270), (50, 270), (100, 180), (50, 90), (50, 90), (50, 270)]
number_9 = [(0, 270), (50, 315), (diagonal, 180), (diagonal, 135), (50, 270), (50, 270), (50, 0)]

#moving the turtle to the start point
turtle.penup()
turtle.left(180)
turtle.forward(400)
turtle.left(180)
turtle.pendown

#telling turtle which numbers it should draw
ind = (number_1, number_4, number_1, number_7, number_0, number_0)

#drawing
for i in ind:
	draw_number(i)
	move_to_next_cell()
