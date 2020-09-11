import turtle
turtle.shape('turtle')
for j in range(10):
    for i in range (4):
        turtle.forward(20+10*(j-1))
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.right(90)
    turtle.pendown()
