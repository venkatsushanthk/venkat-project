import turtle

# Assigning variables
t = turtle.Turtle()
s = turtle.Screen()

# Setting Board
t.pencolor("black")
s.bgcolor("grey")

# Speed of Turtle
t.speed(1000)

# Variables used for the drawing
UnitWidth = int(input("What is the width of the square? "))
Width = 20
Side = UnitWidth * Width

# Functions

# Drawing

# The square
for i in range(0, 4):
    t.fd(Side)
    t.left(90)

t.left(90)

# The rows
for j in range(0, UnitWidth - 1):
    t.fd(Width)
    t.right(90)
    t.fd(Side)
    t.left(180)
    t.fd(Side)
    t.right(90)

t.fd(Width)
t.right(90)

# The columns
for k in range(0, UnitWidth - 1):
    t.fd(Width)
    t.right(90)
    t.fd(Side)
    t.left(180)
    t.fd(Side)
    t.right(90)

# Returns back to home
t.penup()
t.home()

# Exits the turtle graphic screen only when you click on it
turtle.exitonclick()
