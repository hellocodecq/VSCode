"""
    汽车项目课
    1. 建立基础汽车类：brand(品牌)、price(价格)
    2. 基础方法：get_brand(获取品牌)、get_price(获取价格)，复习return的用法
    3. 建立3个车的类，通过列表遍历打印出信息，用变量count计数，便于后续选择车辆
    4. 输入数字买车：数字-1是下标，获取车辆信息，判断是否买得起，要money变量
    5. 购车之后，要开回去，因此要知道多少油，以及油箱容量
    6. 建立属性：oil(油量), box(油箱)
    7. 建立方法：加油(add_oil)、行驶(drive)
    8. 输入距离，循环开车回家，每次行驶1公里
    9. 判断加油：如果drive失败，则加油

    作业：加油1L 100块钱，输出每次加油的金额以及剩余金额，金额不足时无法加油，
         若金额为0并且没到家，则回家失败
"""




class cars():
    def __init__(self, brand, price, oil, box):
        self.brand = brand
        self.price = price
        self.box = box
        self.oil = oil
    def get_brand(self):
        return self.brand
    def get_price(self):
        return self.price
    def drive(self):
        if self.oil > 1:
            self.oil -= 1
            return True
        else:
            print("没油了，请加油")
            return False
    def add_oil(self, oil):
        if (self.oil + oil > self.box):
            print("加油失败！超过油箱上限")
        else:
            self.oil += oil
            print("加油成功！现在的油量：",self.oil)

honda = cars("本田",150000,15,30)
bmw = cars("宝马",300000,20,40)
fort = cars("福特",200000,15,35)

car_list = [honda, bmw, fort]

count = 1
for car in car_list:
    print(count, car.get_brand(), car.get_price())
    count+=1
money = 200000
count = int(input("请输入数字买车："))
mycar = car_list[count-1]

if mycar.get_price() > money:
    print("你没有这么多钱")
    exit()
else:
    print("购车成功！你现在拥有：", mycar.get_brand())

distance = int(input("请输入回家的距离："))
while distance > 0:
    if mycar.drive() == True:
        distance -= 1
        print("行驶了1公里，离家还有：",distance)
    else:
        oil = int(input("请输入要加的油量："))
        mycar.add_oil(oil)

print("成功到家！")