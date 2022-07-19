import math
import turtle

ap = turtle.Turtle()


def draw(t, length, n):
    if n == 0:
        return
    angle = 60
    t.fd(length/3 * n)
    t.lt(angle)
    draw(t, length/3, n-1)
    t.rt(2 * angle)
    draw(t, length/3, n-1)
    t.lt(angle)
    t.bk(length * n)


draw(ap, 45, 3)

turtle.mainloop()
