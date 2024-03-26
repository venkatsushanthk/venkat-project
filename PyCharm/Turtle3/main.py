import turtle

# Assigning long commands to variables
t = turtle.Turtle()
s = turtle.Screen()

# Setting the canvas
s.bgcolor("black")
t.pencolor("white")

# Speed of turtle
t.speed(0)

# Input Variables (for testing)
GridSize = 10
StartRowToken = 5
StartColToken = 5
CellWidth = 30
TokenWidth = 10
Margin = (CellWidth - TokenWidth) / 2
BlockerRow = 1
BlockerCol = 3

# Operational variables
currRowToken = StartRowToken
currColToken = StartColToken


# Functions
def DrawGrid(size):
    t.pendown()
    Side = size * CellWidth
    # The square
    for i in range(0, 4):
        t.fd(Side)
        t.left(90)

    t.left(90)

    # The rows
    for j in range(0, size - 1):
        t.fd(CellWidth)
        t.right(90)
        t.fd(Side)
        t.left(180)
        t.fd(Side)
        t.right(90)

    t.fd(CellWidth)
    t.right(90)

    # The columns
    for k in range(0, size - 1):
        t.fd(CellWidth)
        t.right(90)
        t.fd(Side)
        t.left(180)
        t.fd(Side)
        t.right(90)


def DrawboxFill(x, y, width, color):
    prePenColor = t.pencolor()
    t.pencolor(color)
    t.penup()
    t.goto(x, y)
    t.pendown()
    for a in range(0, width):
        t.fd(width)
        t.left(90)
        t.fd(1)
        t.left(90)
        t.fd(width)
        t.left(180)
    t.pencolor(prePenColor)


def PlotToken(row, col, color):
    x = ((col - 1) * CellWidth) + Margin
    y = ((row - 1) * CellWidth) + Margin
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(0, 4):
        t.fd(TokenWidth)
        t.left(90)
    DrawboxFill(x, y, TokenWidth, color)


def DrawBlocker():
    x = (BlockerCol - 1) * CellWidth
    y = (BlockerRow - 1) * CellWidth
    DrawboxFill(x, y, CellWidth, "grey")


def Clear(r, c):
    PlotToken(r, c, "black")
    PrePenColor = t.pencolor()
    t.pencolor("black")
    t.left(90)
    t.fd(1)
    t.left(180)
    t.fd(TokenWidth + 3)
    t.left(90)
    t.pencolor(PrePenColor)


DrawGrid(GridSize)
DrawBlocker()
t.penup()
PlotToken(StartRowToken, StartColToken, "white")

while True:
    dir = input("Enter Direction. L, R, U, D, 0. ")
    newRowToken = currRowToken
    newColToken = currColToken

    if dir == "L" or dir == "l":
        newColToken = currColToken - 1
    elif dir == "R" or dir == "r":
        newColToken = currColToken + 1
    elif dir == "U" or dir == "u":
        newRowToken = currRowToken + 1
    elif dir == "D" or dir == "d":
        newRowToken = currRowToken - 1
    elif dir == "0":
        break
    else:
        print("Wrong input or ERROR.")

    # Check for boundary/valid conditions
    if (newRowToken < 1
            or newColToken < 1
            or newRowToken > GridSize
            or newColToken > GridSize
            or (newRowToken == BlockerRow) and (newColToken == BlockerCol)):
        print("You hit the boundary. Try again.")
        newRowToken = currRowToken
        newColToken = currColToken

    if (newRowToken != currRowToken) or (newColToken != currColToken):
        # Now move
        Clear(currRowToken, currColToken)
        PlotToken(newRowToken, newColToken, "white")
        currRowToken = newRowToken
        currColToken = newColToken

turtle.exitonclick()
