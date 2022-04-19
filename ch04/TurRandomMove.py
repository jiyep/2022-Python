import turtle as t
import random

sWidth, sHeight = 400, 400
r, g, b, angle, dist, tX, tY = [0]*7
t.shape("turtle")
t.pensize(3)
t.setup(width = sWidth+10, height = sHeight+10)
# t.screensize(sWidth, sHeight)

while True:

    r = random.random()
    g = random.random()
    b = random.random()
    t.pencolor((r, g, b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 200)
    t.left(angle)
    t.forward(dist)

    tX = t.xcor()
    tY = t.ycor()

    if(-sWidth / 2 <= tX and tX <= sWidth /2) and (-sHeight / 2 <= tY and tY <= sHeight /2):
        pass
    else:
        t.penup()
        t.goto(0,0)
        t.pendown()



t.done()



