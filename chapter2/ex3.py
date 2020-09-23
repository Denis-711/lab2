import turtle
turtle.shape('turtle')

def draw_number(movements):
	turtle.pendown()
	for step, angle in movements:
		turtle.forward(float(step))
		turtle.left(float(angle))
		
def move_to_next_cell():
    turtle.penup()
    turtle.forward(100)

#reading instruction how to draw a certain number and transforming it to list of strings
input = open('/home/user1/pythonlabs/lab2/chapter2/config.txt', 'r')
numbers = input.readlines()
for number in range(10):
	numbers[number] = numbers[number].rstrip()
	numbers[number] = numbers[number].split(' ')
	for move in range(len(numbers[number])):
		numbers[number][move] = numbers[number][move].split(',')

#moving the turtle to the start point
turtle.penup()
turtle.left(180)
turtle.forward(400)
turtle.left(180)
turtle.pendown

#telling turtle which numbers it should draw
ind=(1, 4, 1, 7, 0, 0,)

#drawing
for element in ind:
	draw_number(numbers[element])
	move_to_next_cell()
