import turtle
import math
def trikon(t,n,r):
    hs =  r * math.sin(360.0/n*math.pi)


bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()
bob.pensize(1)
bob.color('green')
# draw polypies with various number of sides
size = 40
draw_pie(bob, 5, size)

bob.color('red')
draw_pie(bob, 6, size)

bob.color('pink')
draw_pie(bob, 7, size)

bob.color('blue')
draw_pie(bob, 8, size)

bob.hideturtle()
turtle.mainloop()