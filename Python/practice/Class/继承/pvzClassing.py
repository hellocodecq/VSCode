# 继承
# 泛化

class Plant():      # 植物类, 父类
    def __init__(self, name, hp, pos, pic):
        self.name = name
        self.hp = hp
        self.pos = pos
        self.pic = pic
        print("在", self.pos, "种植了", self.name)
    
    def work(self):
        print(self.name,"工作了")

class Sunflower(Plant):  # 太阳花, 子类
    def __init__(self, name, hp, pos, pic):
        super().__init__(name,hp,pos,pic)
    
    def create_sunshine(self):
        print(self.name,"产生了阳光")

class Beanshooter(Plant):  # 豌豆射手, 子类
    def __init__(self, name, hp, pos, pic):
        super().__init__(name,hp,pos,pic)
    
    def shoot(self):
        print(self.name,"发射了豌豆")

