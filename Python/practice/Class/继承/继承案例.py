class Animal():     # 父类
    def __init__(self, types, sex, age):
        self.type = types
        self.sex = sex
        self.age = age

    def myself(self):
        print("我是个",self.type, "我的性别",self.sex, "我的年龄",self.age)


class Dog(Animal):      # 子类
    def __init__(self, name,  sex, age):
        super().__init__("狗", sex, age)
        self.name = name
        print("我叫",self.name)


class Cat(Animal):
     def __init__(self, name,  sex, age):
        super().__init__("猫", sex, age)
        self.name = name
        print("我叫",self.name)

class Gecko(Animal):
    def __init__(self, name,sex, age):
        super().__init__("壁虎", sex, age)
        self.name = name
        print("我叫",self.name)

    def climb(self):
        print("我会爬墙")


wangcai = Dog("旺财","公", 5)
adai = Cat("阿呆","母",4)

wangcai.myself()
adai.myself()

bihu = Gecko("壁虎", "雄", 1)
bihu.myself()
bihu.climb()







