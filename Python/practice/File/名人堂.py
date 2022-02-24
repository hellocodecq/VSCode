"""
    名人堂
    1. 读取文件(get_data): 保存数据到两个列表中
    2. 显示数据(show_data): 通过下标遍历，遍历出来直接打印
    3. 输入数据(set_score): 判断是否进入榜单(大于最后一个或者长度<10)
    4. 进入榜单: 输入名字，名字不能含有空格
    5. 保存数据: 插入数据、名字到对应位置，保存到文件
    6. 发现问题: 成绩10个以外的也还在，清除掉超限的值
    7. 通过gui显示成绩
    8. 打开一个Pygame游戏，导入此模块，调用函数传入数据
    ---
    作业: 在另一个Pygame项目中导入此模块，完成名人堂功能
"""

from easygui import *

user_list = []
score_list = []

def set_score(score):
    score = int(score)
    if score > score_list[-1] or len(score_list)<10:
        print("大于最后一名，进入榜单")
        name = enterbox("请输入名字: ")
        if ' ' in name:
            print("名字不能含有空格！")
            return 0
        for i in range(len(score_list)):
            if score > score_list[i]:
                score_list.insert(i,score)
                user_list.insert(i, name)
                break
        
        while len(user_list)>10:
            user_list.pop()
            score_list.pop()

        with open("file.txt","w",encoding="utf8") as file:
            for i in range(len(score_list)):
                file.write(user_list[i]+" "+str(score_list[i])+"\n")
        print("保存成功！")
        show_score()

def show_score():
    info = ""
    for i in range(len(user_list)):
        info += user_list[i]+" "+str(score_list[i])+"\n"
    print(info)

def get_score():
    with open("file.txt",encoding="utf8") as file:
        scores = file.readlines()
        for user in scores:
            info = user.split()
            user_list.append(info[0])
            score_list.append(int(info[1]))

if __name__ == '__main__':
    get_score()
    set_score(9)
