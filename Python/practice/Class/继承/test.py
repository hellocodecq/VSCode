# 继承 前半节课


class Planet():     # 天体，父类
    def __init__(self, name, size, types): # 名字和大小
        self.name = name
        self.size = size
        self.types = types
    def info(self):     # 打印天体的信息
        print(self.name, self.types ,"大小: ", self.size)

class Star(Planet): # 恒星，子类
    def __init__(self, name, size, system):
        super().__init__(name, size, "恒星")
        self.system = system
    def whereAmI(self):     # 打印恒星所在的星系
        print(self.name,'在',self.system)

class planet(Planet):   # 行星，子类
    def __init__(self, name, size, father):
        super().__init__(name, size, "行星")
        self.father = father
    def move(self):
        print(self.name,"围着",self.father,"转")


class satellite(Planet): # 卫星，子类
    def __init__(self, name, size):
        super().__init__(name, size, "卫星")

sun = Star("太阳",1300000,"太阳系") # d 130w倍
sun.info()
sun.whereAmI()
earth = planet("地球",1)
earth.info()
moon = satellite("月球", 1/3.7)
moon.info()
