x = -30
y = 0

step = Rect([30, 10])   # 定义砖块

for i in range(10):     # 重复10次，画10块转
    move(x, y)
    step.draw()
    x -= 15
    y -= 10