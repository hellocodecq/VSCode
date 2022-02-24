"""
    只有僵尸类
"""

import time

class zombie():
    def __init__(self, name, hp, pos):
        self.name = name
        self.hp = hp
        self.pos = pos
        print("创建出一只", self.name," 位置：", self.pos)

    def move(self):
        self.pos[1] -= 1
        print(self.name,"前进了1步:", self.pos)
        if self.pos[1] < 0:
            print("僵尸吃掉了你的脑子")
            return True
        return False
    
    def hit(self):
        print(self.name,"被击中了")
        self.hp -= 1
        print(self.name,"血量还剩：",self.hp)
        if self.hp <= 0:
            print(self.name,"被消灭了")
            return True
        return False

normal = zombie("普通僵尸1", 10, [0,11])
normal2 = zombie("普通僵尸2", 10, [0, 15])

zombies = [normal, normal2]

while True:
    for z in zombies:
        if z.move():    
            print("游戏结束")
            exit()
    if zombies[0].hit():
            zombies.pop(0)
    
    time.sleep(1)
    if(len(zombies)==0):
        print("游戏胜利！")
        break