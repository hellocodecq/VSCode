"""
    1. 创建出父类，定义名字、负债，功能：显示自己信息，显示负债
    2. 创建子类，定义名字，实例化父类，定义函数：工作赚钱work
    3. 实例化子类：小王，小王可以调用父类的方法，拥有父类的属性
    4. 小王调用父类方法演示
    5. 小王自己的属性：余额，
    6. 定义方法：查看余额
    7. 定义方法：工作，工作增加余额。
    7. 定义方法：还钱
    --
    案例: 
    1. 动物父类: Animal类，属性：种类、性别、年龄
    2. 动物子类: Dog类，强调用Animal类和Dog类的区别，Animal不能调用Dog的属性了方法
    3. 创建dog对象，dog的特殊方法: bark
    4. 动物子类: Cat类, cat的特殊方法: catch
    5. 动物子类: Gecko(壁虎)，特殊方法：爬墙
    ---
    作业:
    创建出其它动物类，特殊方法
"""


class father():
    def __init__(self, name):
        self.name = name
        self.debt = 50
    def whoAmI(self):
        print("我是",self.name)
    def owe(self):
        print(self.name,"欠债",self.debt,"w")

class son(father):
    def __init__(self, name,money):
        super().__init__(name)
        self.money = money

    def work(self):
        print(self.name,"通过工作赚了10w")
        self.money += 10
        print(self.name,"现在有",self.money,"w")
    
    def mymoney(self):
        print(self.name,"现在有",self.money,"w")
    
    def payback(self):
        if self.debt == 0:
            return 0
        if self.money >= self.debt:
            self.money -= self.debt
            self.debt = 0
            print("还完钱啦！还剩",self.money,"w")
        else:
            print("还了",self.money,"w")
            self.debt -= self.money
            self.money = 0
            print("还欠",self.debt,"w")

    
xiaowang = son("小王",10)
xiaowang.whoAmI()
xiaowang.mymoney()
xiaowang.owe()
xiaowang.work()
xiaowang.payback()
