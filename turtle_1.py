import turtle

turtle.TurtleScreen

num_sides = 3
side_length = 100
angle = 360/num_sides



for i in range(num_sides):
    turtle.forward(side_length)
    turtle.left(angle)

turtle.penup()
turtle.right(270)
turtle.forward(50)

turtle.right(90)

turtle.pendown()

for i in range(num_sides):
    turtle.forward(side_length)
    turtle.right(angle)

turtle.done

var = 100

while var > 0:
    turtle.forward(var)
    turtle.right(90)
    var = var-5




