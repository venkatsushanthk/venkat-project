import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.pencolor("White")

steps = 13
width = 300

loopsBig = width % steps
loopsSmall = steps - loopsBig
step_WidthSmall = width // steps
stepWidthBig = step_WidthSmall + 1

for n in range(0,2):
    t.fd(width)
    t.left(90)

# big steps
for i in range(0, loopsBig):
    t.fd(stepWidthBig)
    t.left(90)
    t.fd(stepWidthBig)
    t.right(90)

# small steps
for j in range(0, loopsSmall):
    t.fd(step_WidthSmall)
    t.left(90)
    t.fd(step_WidthSmall)
    t.right(90)

turtle.exitonclick()
