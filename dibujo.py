import turtle
ventana = turtle.Screen()
soplete=turtle.Turtle()
soplete.shape("turtle")
soplete.color("fuchsia")
soplete.width(2)
soplete.speed(0)
a=10
while True:
    soplete.fd(a)
    soplete.lt(179)
    a=a+10
turtle.done()