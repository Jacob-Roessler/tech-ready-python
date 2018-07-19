import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

def settings():
    t.pd()
    t.speed(0)
    t.pencolor("blue")
    t2.pd()
    t2.speed(0)
    t2.pencolor("orange")
    t3.pd()
    t3.speed(0)
    t3.pencolor("purple")

def draw():
    for x in range(1,1000):
        t.fd(x)
        t2.fd(x)
        t.lt(167)
        t2.rt(162)
        t3.fd(x)
        t3.rt(165)
settings()
draw()