import turtle
turtle.color("red")
turtle.pensize(5)
turtle.penup()
turtle.seth(-90)
turtle.fd(80)
for i in range(9):
    turtle.pendown()
    turtle.seth(0)
    turtle.circle(20*(i+1))
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(20)
