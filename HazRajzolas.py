import turtle
turtle.color("red")

# negyzet
i = 0
while i < 4:
    turtle.forward(100)
    turtle.left(-90)
    i += 1

# haromszog
turtle.setheading(60)
turtle.forward(100)
turtle.setheading(-60)
turtle.forward(100)

turtle.done()