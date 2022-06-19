import turtle
import datetime
import math

def drawGap():              #每条笔画间的空格
    turtle.penup()
    turtle.fd(5)

def drawLine(up):           #绘制单根数码管
    drawGap()
    turtle.pendown()
    turtle.begin_fill() if up else None
    turtle.lt(45)
    turtle.fd(math.sqrt(18))
    turtle.rt(45)
    turtle.fd(34)
    turtle.rt(45)
    turtle.fd(math.sqrt(18))
    turtle.rt(90)
    turtle.fd(math.sqrt(18))
    turtle.rt(45)
    turtle.fd(34)
    turtle.rt(45)
    turtle.fd(math.sqrt(18))
    turtle.end_fill() if up else None
    turtle.rt(135)
    turtle.pu()
    turtle.fd(40)
    drawGap()
    turtle.rt(90)

def realDraw(num, a):#决定这根管是否上色，为后续绘制减少重复代码量
    if num in a:
        drawLine(True)
    else:
        drawLine(False)

def drawNumber(num, dot):       #依次走过七根数码管
    realDraw(num, [2,3,4,5,6,8,9])
    realDraw(num, [0,1,3,4,5,6,7,8,9])
    realDraw(num, [0,2,3,5,6,8,9])
    if dot:                     #绘制小数点
        turtle.pendown()
        turtle.fd(5)
        turtle.penup()
        turtle.fd(-5)
    realDraw(num, [0,2,6,8])
    turtle.lt(90)
    realDraw(num, [0,4,5,6,8,9])
    realDraw(num, [0,2,3,5,6,7,8,9])
    realDraw(num, [0,1,2,3,4,7,8,9])
    turtle.penup()
    turtle.lt(180)
    turtle.fd(20)


def drawDate(date):             #绘制出一组字符串
    turtle.color("red")
    for i in date:
        if i == '-':
            turtle.write('年', font=("Arial", 60, "normal"))
            turtle.pencolor("green")
            turtle.fd(100)
        elif i == '=':
            turtle.write('月', font=("Arial", 60, "normal"))
            turtle.pencolor("yellow")
            turtle.fd(100)
        elif i == '+':
            turtle.write('日',font=("Arial", 60, "normal"))
        elif i == '.':
            drawNumber(i,True)
        else:
            drawNumber(eval(i), False)


def main(idx):                     #初始化turtle
    turtle.setup(1000, 350, 200, 200)
    turtle.penup()
    turtle.fd(-400)
    turtle.pensize(1)
    if idx == 1:
        try:
            Number = eval(input("请输入你想显示的数字"))
            drawDate(str(Number))
            turtle.bye()
        except SyntaxError:
            print("输入错误,请输入数字!")

    elif idx == 3:
        drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
        turtle.bye()

    elif idx == 2:
        datestr = str(input("请输入想显示的时间"))
        drawDate(datestr)
        turtle.bye()
