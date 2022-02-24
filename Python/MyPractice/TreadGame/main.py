import easygui
import pygame
import threading
import easygui

from Chara import Chara
from tool import *

# 建立游戏基础窗口
pygame.init()
screen = pygame.display.set_mode((600,400))
screen.fill((255,255,255))
pygame.display.set_caption("比赛")

# 导入图片
p_enemy = pygame.image.load(r'Python\practice\Class\plane\src\enemy1.png')
bg = pygame.image.load(r"Python\MyPractice\TreadGame\src\bg.png")
cheer = pygame.mixer.Sound(r"Python\MyPractice\TreadGame\src\cheer.wav")

# 创建操作对象
enemy = Chara(p_enemy, [0,0],[480,320])

# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        
# 输入窗口线程
code = read_code()
def enter():
    global code
    while True:
        try:
            code = easygui.textbox(text=code)   # 输入代码
            if code == None:        # 处理退出窗口，避免上面一行text错误
                code = ''
            enemy.restart()     # 使角色归位
            exec(code)          # 执行输入的程序
            save_code(code)     # 保存输入的代码，避免异常退出丢失程序
            if enemy.flag:      # 判断有没有离开地图
                easygui.msgbox("错误！离开地图",'错误！')
        except:
            easygui.msgbox('代码错误！','错误!')
        if enemy.arrive() and enemy.flag==False: # 如果到达目的地并且没有离开过地图
            cheer.play()
            easygui.msgbox('你赢了','真棒！')
            clear_code()
            enemy.restart()
            break

# 创建输入窗口，多线程
Enter = threading.Thread(target=enter)
Enter.setDaemon(True)
Enter.start()

# 游戏循环
while True:
    screen.blit(bg,(0,0))
    screen.blit(enemy.img,enemy.pos)

    """
        如果离开地图, enemy.flag = True
    """   
        

    handleEvent()
    pygame.display.update()