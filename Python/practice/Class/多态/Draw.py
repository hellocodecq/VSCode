from turtle import *


def moveto(x, y):
    penup()
    goto(x, y)
    pendown()

class Shape():
    def __init__(self, name, length, color):
        self.name = name
        self.length = length
        self.color = color
    
    def draw(self):
        print("画一个边长",self.length,"的", self.name)

class Square(Shape):
    def __init__(self, length,color='white'):
        super().__init__('正方形',length,color)
    
    def draw(self):
        for i in range(4):
            fd(self.length)
            rt(90)

class Circle(Shape):
    def __init__(self, length,color='white'):
        super().__init__('圆',length,color)
    def draw(self):
        circle(self.length)

class Rectangle(Shape):
    def __init__(self,w, h,color='white'):
        super().__init__("长方形", (w,h),color)
    def draw(self):
        for i in range(2):
            fd(self.length[0])
            rt(90)
            fd(self.length[1])
            rt(90)

class nSquare(Shape):
    def __init__(self, n, length, head=1,color='white'):
        self.n = n
        name = str(n)+"边形"
        self.head = head
        super().__init__(name, length,color)
    def draw(self):
        ang = 360/self.n
        if self.head < 1:
            ang = -ang
        for i in range(self.n):
            fd(self.length)
            rt(ang)


speed(0)


floor = nSquare(3,100,0)
body = Square(100)
door = Rectangle(30,50)
window = Circle(15)
step =  Rectangle(30,10)
chimney_down = Rectangle(30, 150)
chimney_middle = Square(20)
chimney_up = nSquare(3, 30, 0)


floor.draw()
body.draw()
moveto(35,-50)
door.draw()
moveto(50,15)
window.draw()

moveto(70, -20)
chimney_middle.draw()

x = -30
y = 0

for i in range(10):
    moveto(x,y)
    step.draw()
    x -= int(step.length[0]/2)
    y -= step.length[1]

moveto(100,50)
chimney_down.draw()
moveto(105,70)
chimney_middle.draw()
moveto(100,70)
chimney_up.draw()














mainloop()
