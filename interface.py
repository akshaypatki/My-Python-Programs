import math
import turtle
bob=turtle.Turtle()

def rectangle():
    a = input('what is the length and breadth of square', )
    b = input('What is the width of the rectangle', )
    bob.fd(int(a))
    bob.lt(90)
    bob.fd(int(b))
    bob.lt(90)
    bob.fd(int(a))
    bob.lt(90)
    bob.fd(int(b))
    bob.lt(90)


def polygon():
    n= int(input ('how many sides?',))
    l = int(input ('what is the length of a side',))
    angle = 360/n
    while n:
        bob.fd(l)
        bob.lt(angle)
        n-=1

def circle():
    r = int(input('radius?',))
    circumfurance = 2* math.pi * r
    l = circumfurance / 360
    n = 360
    while n:
        bob.fd(l)
        bob.lt(1)
        n -= 1

#rectangle()
#circle()
polygon()
turtle.mainloop()