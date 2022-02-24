from tkinter import NS
from turtle import *
speed(0)
class shape():
    def __init__(self, name, length):
        self.name = name
        self.length = length
    
    def draw(self):     # 画
        print("画一个边长", self.length, "的", self.name)


class Square(shape):
    def __init__(self, length):
        super().__init__(  '正方形', length   )
    
    def draw(self):
        for i in range(4):
            fd(self.length)
            rt(90)


class Rect(shape):   # 矩形
    def __init__(self, length):
        super().__init__(  '矩形', length   )


    def draw(self):
        # 画矩形
        # self.length：
        print(self.length)
        for i in range(2):
            fd(self.length[0])
            rt(90)
            fd(self.length[1])
            rt(90)

class nSuqare(shape):   # 多边形
    def __init__(self, num, length, head):
        self.head = head
        self.num = num
        super().__init__(   str(self.num)+"边形",   length )
    
    def draw(self):
        ang = 360 / self.num
        if self.head==0:        # 朝着上面
            ang = -ang

        for i in range(self.num):
            fd(self.length)
            rt(ang)
            

def move(x, y):     # 移动
    pu()
    goto(x, y)
    pd()
        

wbx = nSuqare(   3, 100 ,  0  ) # 三角形
wbx.draw()

body = Square(100)      # 正方形
body.draw()



move(35,-50)
door = Rect([30,50])     # 门
door.draw()
##################################################
x = -30
y = 0

step = Rect([30, 10])   # 定义砖块

for i in range(10):     # 重复10次，画10块转
    move(x, y)
    step.draw()
    x -= 15
    y -= 10
####################################################

move(100,50)
yc_down = Rect([30,150])
yc_down.draw()


move(105,70)
yc_mid = Square(20)
yc_mid.draw()

bk(5)
yc_up = nSuqare(3, 30,0)
yc_up.draw()

###########################################
pencolor('red')

move(70,-15)
yc_mid.draw()
move(50,10)
circle(20)


hideturtle()
mainloop()