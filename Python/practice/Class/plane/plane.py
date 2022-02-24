import pygame
import time
from random import *


time_now = time.time()
interval = 0.3


screen = pygame.display.set_mode((480,650))
screen.fill((255,255,255))
pygame.display.set_caption("飞机大战")

bg = pygame.image.load("./Python/Class/plane/src/bg.png")
e1 = pygame.image.load("./Python/Class/plane/src/enemy1.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def create_plane():
    global planelist, time_now
    if time.time() - time_now >= interval:
        time_now = time.time()
        # randplane = randint(0,10)
        # if randplane <= 6:
        print("产生飞机")
        planelist.append(Plane(e1, 1, [randint(0,400),-100]))
        

class Plane():
    def __init__(self, picture, hp, pos):
        self.pic = picture
        self.hp = hp
        self.pos = pos
    def fly(self):
        self.pos[1] += 1
        if self.pos[1] >= 700:
            return True
        return False


planelist = []
while True:
    screen.blit(bg,(0,0))
    create_plane()
    for plane in planelist:
        screen.blit(plane.pic, plane.pos)
        if plane.fly():
            del plane

    pygame.display.update()
    handleEvent()