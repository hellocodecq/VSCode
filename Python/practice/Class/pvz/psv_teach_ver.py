"""
    僵尸类+植物类, 难度较大
"""

class zombie():
    def __init__(self, name, hp, pos):
        self.name = name
        self.hp = hp
        self.pos = pos
        self.info()
    
    def info(self):
        print("在", self.pos, "产生一只",self.name)
    
    def move(self):
        self.pos[1] -= 1
        print(self.name, "前进了1步:",self.pos)
        if self.pos[1] <= 0:    # 走进房子里了
            return True
        else:
            return False
    
    def hit(self):
        self.hp -= 1
        print(self.name,"血量还剩：",self.hp)
        if self.hp <= 0:
            return True
        else:
            return False 

    def back(self):         # 僵尸后退
        self.pos[1] += 1
        print("僵尸被挡住了")


class shooter():
    def __init__(self, name, hp, pos):
        self.name = name
        self.hp = hp
        self.pos = pos
        print("在",self.pos,"种植了",self.name)

    def shoot(self):    # 射击
        print(self.name,"发射了一枚子弹")
        return True

    def ate(self):# 植物被吃
        self.hp -= 1
        print(self.name,"被吃了一口, 还剩",self.hp,"点血量")
        if self.hp <= 0:
            return True
        else:
            return False


                            #   行 列
normal = zombie("普通僵尸", 10, [0, 9])
beanshooter = shooter("豌豆射手",3 ,[0,2])

while True:
    # 如果植物血量大于0         植物射击
    # a = input()
    if beanshooter.hp > 0 and beanshooter.shoot() :
        if normal.hit():        # 僵尸被击中
            print("游戏胜利")   # 僵尸死亡
            exit()
    if normal.move() == True:       # 僵尸移动
        print("僵尸吃掉了你的脑子") 
        exit()
    
    if normal.pos == beanshooter.pos and beanshooter.hp > 0:   # 植物抵挡僵尸
        normal.back()
        if beanshooter.ate() == True:
            print("植物被吃掉了")
        