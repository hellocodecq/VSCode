from turtle import *


# 画一个礼物盒子
pensize(5)
speed(0)

begin_fill()
color('yellow','red')

# begin_fill()        # 盖子
# for i in range(2):
#     fd(120)
#     rt(90)
#     fd(40)
#     rt(90)
# end_fill()

# 盒子
# pu()
# goto(10,-40)
# pd()
# begin_fill()
# for i in range(4):
#     fd(100)
#     rt(90)
# end_fill()

begin_fill()
for i in range(4):
    fd(120)
    rt(90)
    fd(120)
    rt(90)
end_fill()

pu()
goto(60,0)
pd()
color("yellow","orange")
pensize(2)
begin_fill()
seth(160)
fd(40)
rt(70)
fd(40)
goto(60,0)
end_fill()

begin_fill()
seth(20)
fd(40)
lt(70)
fd(40)
goto(60,0)
end_fill()

seth(-90)
pensize(10)
fd(120)
pu()
goto(0, -60)
pd()
seth(0)
fd(120)


hideturtle()
mainloop()