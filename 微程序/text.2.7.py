import turtle
import math
turtle.pencolor("red")
turtle.penup()
turtle.seth(270)
turtle.fd(100)
turtle.pendown()
for i in range(3):
    turtle.seth(30 + (120*i))
    turtle.fd(300)
turtle.seth(0)
turtle.penup()
turtle.fd(math.sqrt(100**2 - 50**2) * 2)
turtle.pendown()
for i in range(3):
    turtle.seth(90 + 120*i)
    turtle.fd(300)
