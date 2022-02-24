from turtle import *


def fire():
    seth(-135)
    begin_fill()
    for i in range(2):
        fd(30)
        rt(90)
        fd(20)
        rt(90)
    end_fill()

    seth(-45)
    begin_fill()
    for i in range(2):
        fd(30)
        lt(90)
        fd(20)
        lt(90)
    end_fill()


# 画一个鞭炮
pensize(5)
color('yellow','red')

rt(90)

pu()
goto(0,-20)
pd()
fire()


goto(0,-60)
fire()


goto(0,-100)
fire()

goto(0,-140)
fire()

goto(0,-180)
fire()



hideturtle()
mainloop()
