import turtle
import random
import time

t = turtle.Turtle()
def settings(t):
    t.speed(10)

def mazeOutline(t):
    t.pencolor("white")
    t.goto(250,250)
    t.pencolor("black")
    t.lt(180)
    t.fd(500)
    t.lt(90)
    t.fd(500)
    t.lt(90)
    t.fd(500)
    t.lt(90)
    t.fd(450)
def mazeBuild(t):
    turns = 0
    for x in range(250):
        while t.xcor() < 500 and t.ycor() < 500 and turns < 4:
            t.fd(random.randint(0,80))
            t.lt(90)


settings(t)
mazeOutline(t)
mazeBuild(t)
time.sleep(10)