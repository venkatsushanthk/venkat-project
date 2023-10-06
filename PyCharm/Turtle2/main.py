import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.pencolor("black")
s.bgcolor("grey")

t.speed(1000)

UnitWidth = int(input("What is the width of the square? "))
Width = 20
Side = UnitWidth * Width

for i in range(0, 4):
    t.fd(Side)
    t.left(90)

t.left(90)

for j in range(0, UnitWidth - 1):
    t.fd(Width)
    t.right(90)
    t.fd(Side)
    t.left(180)
    t.fd(Side)
    t.right(90)

t.fd(Width)
t.right(90)

for k in range(0, UnitWidth - 1):
    t.fd(Width)
    t.right(90)
    t.fd(Side)
    t.left(180)
    t.fd(Side)
    t.right(90)

t.penup()
t.home()

turtle.exitonclick()
