import pygame
from random import *
import time

screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))
pygame.display.set_caption("植物大战僵尸v0.3")

bg = pygame.image.load("./Python/Class/pvz/src/gameBg.png")
zombie1 = pygame.image.load("./Python/Class/pvz/src/zombie1.png")


class zombie():
    def __init__(self, name, hp, pos, pic):
        self.name = name
        self.hp = hp
        self.pos = pos
        self.pic = pic
        print("创建出一只", self.name," 位置：", self.pos)

    def move(self):
        self.pos[0] -= 0.1
        print(self.name,"前进了1步:", self.pos)
        if self.pos[0] < 0:
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

z1 = zombie("普通僵尸", 10, [500, 100], zombie1)
z2 = zombie("普通僵尸2", 10,[800,300], zombie1)

z_list = [z1, z2]

time_now = time.time()
def create_zombie():        # 创建僵尸
    global z_list, time_now
    if time.time() - time_now >= 2:     # 过了2s
        time_now = time.time()
        z_list.append(zombie("普通僵尸",10, [randint(800,900), randint(0,500)], zombie1))
time_hit = time.time()
while True:
    create_zombie()     # 调用函数，添加僵尸
    screen.blit(bg,(0,0))
    
    for z in z_list:
        screen.blit(z.pic, z.pos)
        if z.move() == True:
            z_list.remove(z)
            del z

    if time.time() - time_hit >=1:
        time_hit = time.time()
        if len(z_list) > 0 and z_list[0].hit()  == True:
            del z_list[0]
    
    """
        作业：通过随机数产生不同僵尸：
        0~5：zombie1，血量10
        6~8：zombie2，血量15
        9~10：zombie3，血量20
        11：zombie4，血量30
    """
    
    for event in pygame.event.get():        # 退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()


