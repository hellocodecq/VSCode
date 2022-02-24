from random import *
import time

"""
    打字母的小游戏
"""

time_delay = 3  # 3s产生一个字母
letter_list = []    # 产生的所有字母
time_now = time.time()

class Letter():          
    def __init__(self, letter, img, pos,spd):
        self.letter = letter    # 字母
        self.img = img          # 字母图片
        self.pos = pos          # 字母位置，列表，x，y
        self.spd = spd          # 下落速度
    
    def fall(self):             # 下落
        self.pos[1] += self.spd
        return self.pos[1]      # 返回自己的y坐标，判断是否到达底部
    
    def get_letter(self):       # 获取字母
        return self.letter

def random_letter():
    rand = chr(randint(ord('a'), ord('z')))  # 产生随机字母
    print(rand)
    return rand

def create_letter():
    global time_now
    if time.time() - time_now >= time_delay:  # 到了时间，产生新的字母
        time_now = time.time()
        letter_list.append(random_letter())
        print(letter_list)

        


