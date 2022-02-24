"""
僵尸类: 添加到列表中, 遍历列表不断前进, 列表第一只会受到伤害
"""

class zombie():
    def __init__(self, name, hp, pos):
        self.name = name
        self.hp = hp
        self.pos = pos
        print("在",self.pos,"产生了1只",self.name)
    def move(self):
        self.pos[1] -= 1
        print(self.name,"前进了1步", self.pos)
        if self.pos[1] < 0:
            print(self.name,"吃掉了你的脑子")
            return True
        else:
            return False
    def hitted(self):
        self.hp -= 1
        print(self.name,"被击中了")
        print(self.name,"的hp还剩",self.hp)
        if self.hp <= 0:
            print(self.name,"被消灭了")
            return True
        return False

class shooter():
    def __init__(self, name, hp, pos):
        self.name = name
        self.hp = hp
        self.pos = pos
        print("在",self.pos,"产生了", self.name)
    def shoot(self):
        print(self.name,"射击了")
    def ate(self):
        self.hp -= 1
        print(self.name,"被咬了")
        print(self.name, "的hp还剩", self.hp)
        if self.hp <= 0:
            print(self.name, "被吃掉了")
            return True
        return False

normal = zombie("普通僵尸",10,[0, 10])
normal2 = zombie("普通僵尸2",10,[0, 15])
bean = shooter("豌豆射手",3, [0,0])

zombies = [normal,normal2] 
plants = [bean]
while True:
    a = input()
    for p in plants:
        p.shoot()
        if zombies[0].hitted():
            zombies.pop(0)
            if len(zombies)==0:
                print("游戏胜利")
                exit(0)
    for z in zombies:
        if z.move():
            print("游戏结束")
            exit(0)
        for p in plants:
            if p.pos == z.pos:
                if p.ate():
                    plants.remove(p)
                z.pos[1]+=1
                

        


