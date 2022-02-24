import pygame
from pvzClassing import *
from hipygame import *

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("植物大战僵尸")

bg = pygame.image.load("Python\\practice\\Class\\继承\\src\\bg.png")

p_sunflower = pygame.image.load("Python\\practice\\Class\\继承\\src\\sunflower.png")

sunflower = Sunflower("太阳花",3,(100,100),p_sunflower)
plant_list = [sunflower]
chose = None
game_list = []
def handleEvent():
    global chose,game_list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            for p in plant_list:
                if in_rect((x,y), (p.pos[0],p.pos[1],p.pic.get_width(),p.pic.get_height())) :
                    print("选中",p)
                    chose = p
        
                
        if event.type == pygame.MOUSEBUTTONUP and chose != None:
            print("放下植物", chose)
            if chose.name == "太阳花":
                s = Sunflower("太阳花",3,pygame.mouse.get_pos(),p_sunflower)
                game_list.append(s)
            chose = None
    if chose != None:
            screen.blit(chose.pic,pygame.mouse.get_pos())


while True:
    screen.blit(bg,(0,0))
    screen.blit(sunflower.pic,sunflower.pos)

    for p in game_list:
        screen.blit(p.pic, p.pos)

    handleEvent()

    pygame.display.update()