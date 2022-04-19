import turtle as t
import random

t.shape("turtle")

#거북이 사이즈,크기,색,각도 램덤함수
def screenLeftClick(x,y):
    tSize = random.randrange(1, 10)
    t.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    t.color((r, g, b))
    tAngle = random.randrange(8, 360)

    t.goto(x,y)
    t.left(tAngle)
    t.stamp()

    print("x = ",x,", y = ",y)

#크기,각도,색 초기설정
tSize, tAngle = 0, 0
r, g, b = 0.0, 0.0, 0.0

#함수호출
t.onscreenclick(screenLeftClick)

t.done()


