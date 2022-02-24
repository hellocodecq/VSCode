import time

class Chara():
    def __init__(self, img, pos, target, flag = False):
        self.img = img
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.target = target
        self.flag = flag
    
    def down(self):
        self.pos[1] += 80
        time.sleep(0.5)
        

    def up(self):
        self.pos[1]  -= 80
        time.sleep(0.5)
    
    def left(self):
        self.pos[0] -= 80
        time.sleep(0.5)
    
    def right(self):
        self.pos[0] += 80
        time.sleep(0.5)
    
    def restart(self):
        self.pos = [self.x, self.y]
        self.flag = False
        time.sleep(0.5)


    def arrive(self):
        print(self.pos, self.target)
        if self.pos == self.target:
            return True
        return False