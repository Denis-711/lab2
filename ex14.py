import turtle
turtle.shape('turtle')
def star(n):
	angle=(n-2)*180/n
	for i in range (n):
		turtle.forward(200)
		turtle.left(180-angle/3)
	turtle.right(180)
turtle.left(180)
star(5)

turtle.penup()
turtle.forward(400)
turtle.left(180)
turtle.pendown()

star(11)
