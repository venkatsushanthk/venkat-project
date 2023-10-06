import turtle

# Assigning variables
t = turtle.Turtle()
s = turtle.Screen()

# Setting Board
t.pencolor("black")
s.bgcolor("grey")

# Speed of Turtle
t.speed(0)

# Variables used for the drawing
UnitWidth = 5
# int(input("What is the width of the square? "))
Width = 20
Side = UnitWidth * Width


# Functions
def ColorGrid(row, column):
    x = (column - 1) * Width
    y = (row - 1) * Width
    t.penup()
    t.goto(x, y)
    t.pendown()
    for a in range(0, Width // 2):
        t.left(90)
        t.fd(1)
        t.right(90)
        t.fd(Width)
        t.left(90)
        t.fd(1)
        t.left(90)
        t.fd(Width)
        t.left(180)


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

OddRows = (UnitWidth + 1) // 2
EvenRows = UnitWidth // 2
for r1 in range(0, OddRows):
    for c1 in range(0, OddRows):
        row1 = r1 * 2 + 1
        col1 = c1 * 2 + 1
        ColorGrid(row1, col1)

for r2 in range(0, EvenRows):
    for c2 in range(0, EvenRows):
        row2 = r2 * 2 + 2
        col2 = c2 * 2 + 2
        ColorGrid(row2, col2)

# Returns back to home
t.penup()
t.home()

# Exits the turtle graphic screen only when you click on it
turtle.exitonclick()
