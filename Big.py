from operator import lt
import turtle


def drawDa(size):
    turtle.lt(40)
    turtle.fd(size)
    turtle.pu()
    turtle.lt(90)
    turtle.circle(size/2, 90)
    turtle.lt(90)
    turtle.pd()
    turtle.fd(size/2)
    turtle.circle(-size/2, 90)
    turtle.pu()
    turtle.lt(180)
    turtle.circle(size/2, 90)
    turtle.lt(180)
    turtle.pd()
    turtle.circle(size/2,90)

def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 15
    turtle.pensize(pythonsize)
    b = input("颜色")
    turtle.pencolor(b)
    turtle.seth(-40)
    a = int(input("大小"))
    drawDa(a)


