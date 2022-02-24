"""
    1. 重新写上次的僵尸类（看情况复制粘贴也可以）
    2. 添加属性：pic，保存图片
    2. 建立pygame框架，导入背景、角色(1个僵尸就行)
    3. 建立一个僵尸，添加到僵尸列表
    4. 遍历僵尸列表，移动
    5. 使用函数创建僵尸，设定产生僵尸的时间差(interval)，自动装填僵尸
    6. 僵尸走到最左边，pop删除僵尸对象
    7. 每2s，僵尸列表的第一只受到伤害
    拓展：30s后，停止产生僵尸，如果僵尸死完(列表为空)，显示游戏胜利，僵尸吃到脑子，游戏失败


    作业：通过随机数产生不同僵尸：
        0~5：zombie1，血量10
        6~8：zombie2，血量15
        9~10：zombie3，血量20
        11：zombie4，血量30
"""

import pygame
import time
from random import *


time_now = time.time()
hit_time = time.time()
interval = 3


screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))
pygame.display.set_caption("植物大战僵尸")

bg = pygame.image.load("Python/Class/pvz/src/gameBg.png")
e1 = pygame.image.load("Python/Class/pvz/src/zombie1.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def create_zombie():
    global zombielist, time_now
    if time.time() - time_now >= interval and len(zombielist) <=2:
        time_now = time.time()
        print("产生僵尸")
        zombielist.append(Zombie("普通僵尸", 10, [800,randint(0,500)],e1))
        
class Zombie():
    def __init__(self, name, hp, pos, pic):
        self. name = name
        self.hp = hp
        self.pos = pos
        self.pic = pic
        print("创建出一只", self.name," 位置：", self.pos)

    def move(self):
        self.pos[0] -= 0.01
        # print("前进了1步:", self.pos)
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




zombielist = []
while True:
    screen.blit(bg,(0,0))

    # 创建僵尸，添加到列表
    create_zombie()

    # 遍历所有僵尸，绘制，移动
    for zombie in zombielist:
        screen.blit(zombie.pic, zombie.pos)
        
        if zombie.move():   # 走到最左边删除
            print("僵尸吃掉了你的脑子")

            # 从列表移除僵尸
            zombielist.remove(zombie)
            del zombie      # 删除这只僵尸
            print("剩余僵尸：", len(zombielist))
    
    # 每2s，第一只僵尸收到伤害
    if len(zombielist)>0 and time.time()-hit_time >= 2:
        if zombielist[0].hit():
            zombielist.pop(0)
        hit_time = time.time()

    pygame.display.update()
    handleEvent()