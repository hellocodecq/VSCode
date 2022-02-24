import pygame

screen = pygame.display.set_mode((960,720))

#碰撞检测
def hit(e,h,e_x,e_y,h_x,h_y):
    if h_x-e.get_width()<e_x<h_x+h.get_width() and \
        h_y-e.get_height()<e_y<h_y+h.get_height():
        return True

#文字书写
def write(str,size,pos):
    T = pygame.font.SysFont("simsunnsimsun",size)
    t =T.render(str,True,(255,255,255))
    screen.blit(t,pos)

def in_rect(pos, rect):
    x,y = pos
    rx,ry,w,h = rect
    if rx<x<rx+w and ry<y<ry+h:
        return True
    return False

def rect_in_rect(rect1, rect2):
    r1x, r1y,r1w,r1h = rect1
    r2x, r2y, r2w, r2h = rect2
    if r1x-r2w < r2x < r1x+r1w and \
        r1y-r2h < r2y < r1y+r1h:
        return True
    return False
