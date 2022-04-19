import turtle as t
import random

t.shape("turtle")

def tRandom(x,y):
    t.goto(x, y)

    tSize = random.randrange(1, 10)
    t.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    t.color((r, g, b))

    t.stamp()


#크기,각도,색 초기설정
tSize, tAngle = 0, 0
r, g, b = 0.0, 0.0, 0.0

t.onscreenclick(tRandom)

t.done()
