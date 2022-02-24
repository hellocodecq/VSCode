"""
    星球
    恒星
    行星
    卫星
"""

class Planet():     # 星球
    def __init__(self, name, kinds, size):
        self.name = name
        self.kinds = kinds
        self.size = size
    def get_name(self):
        print("我是",self.name)
    def get_kinds(self):
        print("我的种类是",self.kinds)
    def get_size(self):
        print("我的大小是",self.size)

class Star(Planet):     # 恒星
    def __init__(self, name, size, system):
        super().__init__(name, "恒星", size)
        self.system = system
    def mySystem(self):
        print(self.name,"在",self.system)
    
class planet(Planet):       # 
    def __init__(self, name, size, star):
        super().__init__(name, "行星", size)
        self.star = star
    
    def myStar(self):
        print(self.name,"围着", self.star,"转")

class satellite(Planet):
    def __init__(self, name, size, planet):
        super().__init__(name, "卫星", size)
        self.planet = planet

    def myPlanet(self):
        print(self.name,"围着",self.planet,"转")

star = Star("太阳",5000,"银河系")
star.mySystem()
earth = planet("地球",10,"太阳")
earth.myStar()
moon = satellite("月球",1, "地球")
moon.myPlanet()