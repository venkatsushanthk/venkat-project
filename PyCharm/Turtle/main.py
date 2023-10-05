# This entire code can be run on PyCharm and needs you to download the turtle package

import turtle

# Assigning big commands to small variables
t = turtle.Turtle()
s = turtle.Screen()

# Assigning colors
s.bgcolor("black")
t.pencolor("White")

# Inputting variables to draw
width = int(input("What is the width of the shape? "))
steps = int(input("What is the number of steps you want to take to get back to the start? "))

# If statements
if width % steps == 0:
    # The width of each step
    stepWidthBig = width / steps
    stepWidthSmall = stepWidthBig
    loopsSmall = 0
elif width % steps != 0:
    # This is the loops for the big steps
    loopsBig = width % steps
    # This is the loops for the small steps
    loopsSmall = steps - loopsBig
    # The width of each step
    stepWidthSmall = width // steps
    # When the remainder of width / steps != 0 then we will have smaller steps
    stepWidthBig = stepWidthSmall + 1

# Drawing
for n in range(0, 2):
    t.fd(width)
    t.left(90)

# loopsBig
for i in range(0, loopsBig):
    # The steps will be larger here
    t.fd(stepWidthBig)
    t.left(90)
    t.fd(stepWidthBig)
    t.right(90)

# loopsSmall
for j in range(0, loopsSmall):
    # The steps will be smaller here and won't run when the remainder of width /steps = 0
    t.fd(stepWidthSmall)
    t.left(90)
    t.fd(stepWidthSmall)
    t.right(90)

# This makes sure the turtle tab only closes when you click on it
turtle.exitonclick()
