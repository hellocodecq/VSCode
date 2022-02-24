from easygui import *

class person():
    def __init__(self, name, ID, sex):
        self.name = name
        self.sex = sex
        self.ID = ID

    def save_info(self):
        with open("info.txt", 'a+',encoding="utf8") as file:
            file.write(self.name+" "+self.ID+" "+self.sex+"\n")


stu_list = []
with open("info.txt", encoding="utf8") as file:
    for line in file:
        info = line.split()
        stu = person(info[0],info[1], info[2])
        stu_list.append(stu)
""" 读取完可以遍历出来，更加直观的看出里面储存的东西 """

while True:
    cmd = buttonbox("请选择功能","学生管理系统",("查看信息","添加信息",'退出'))

    if cmd=="退出":
        break
    elif cmd == "查看信息":
        ID = enterbox("请输入ID","查看信息")
        for stu in stu_list:
            if ID == stu.ID:
                msgbox("姓名："+stu.name+"\nID："+stu.ID+"\n性别："+stu.sex)
                break
        else:
            msgbox("没有这个人：",ID)
    elif cmd == "添加信息":
        ID = enterbox("请输入ID：")
        name = enterbox("请输入名字 ")
        sex = enterbox("请输入性别")

        stu = person(name, ID, sex)
        stu.save_info()
        stu_list.append(stu)
