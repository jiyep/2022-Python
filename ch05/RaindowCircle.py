import turtle as t
import random

t.shape("turtle")

r, g, b = [0]*3
sWidth, sHeight = 500, 500


t.setup(width = sWidth+50, height = sHeight + 50)
t.screensize(sWidth, sHeight)
t.penup()
t.goto(0, -sHeight/2)
t.pendown()
t.speed(5)

for radius in range(1, 250):

    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor((r, g, b))

    t.circle(radius)

t.done()
