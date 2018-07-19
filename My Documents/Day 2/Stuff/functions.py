import turtle
import random
import time

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t = [t1,t2]
for x in t:
    x.pd()
    x.speed(0)
    x.pensize(1)
    x.pencolor("blue")
    if x == t[1]:
        x.pencolor("orange")

def fun():
    for x in range(0,200):
        t[0].fd(x)
        t[1].fd(x+5) 
        t[0].lt(30) 
        t[1].rt(45)
fun()
time.sleep(5)
