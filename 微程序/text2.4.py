import turtle
for i in range(3):
    turtle.seth(120 * i)
    turtle.fd(200)
turtle.seth(0)
turtle.fd(100)
for i in range(3):
    turtle.seth(60 * (2*i + 1))
    turtle.fd(100)
