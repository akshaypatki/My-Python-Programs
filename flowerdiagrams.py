import turtle
import math

ap = turtle.Turtle()


def arc(t, r, angle):
    circumfurance = 2 * math.pi * int(r)
    l = circumfurance / 360
    n = angle
    while n:
        t.fd(l)
        t.lt(1)
        n -= 1


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, r, angle, n):
    """ t is the turtle reference
        r is the radius of the flower/petal/arc
        angle is the degrees that subtends the arc
        n is the the number of petals"""
    for i in range(n):
        petal(t, r, angle)
        t.lt(float(360.0 / n))


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


move(ap, -300)
flower(ap, 60.0, 60.0, 7)
move(ap, 100)
flower(ap, 40.0, 80.0, 10)
move(ap, 100)
flower(ap, 140.0, 20.0, 20)
move(ap, 100)
flower(ap, 60, 30, 6)
move(ap, 100)
flower(ap, 60, 60, 6)
move(ap, 150)
flower(ap, 60, 90, 6)

ap.hideturtle()
turtle.mainloop()
