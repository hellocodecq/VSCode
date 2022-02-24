from turtle import *

speed(0)

# 画一个红包
pensize(5)
color('yellow','red')
begin_fill()
for i in range(2):
    fd(200)
    rt(90)
    fd(300)
    rt(90)
end_fill()

goto(50,-50)
goto(150,-50)
goto(200,0)


pu()
goto(100, -250)
pd()
circle(50)

pu()
goto(65, -240)
pd()

write("福", font=("微软雅黑", 50))




hideturtle()
mainloop()