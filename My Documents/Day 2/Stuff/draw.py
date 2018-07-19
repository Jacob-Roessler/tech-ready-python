import turtle
import random
import time

t = turtle.Turtle()
def settings(t):
    t.speed(0)
def draw(t):
    for x in range(500):
        t.fd(x)
        t.lt(135)
settings(t)
draw(t)