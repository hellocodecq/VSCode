from easygui import *

name = enterbox("请输入账号：")
pswd = passwordbox("请输入密码：")

print(name)
print(pswd)

if name == "abc" and pswd == "123":
    msgbox("欢迎登录")
else:
    msgbox("账号密码错误！")
    exit()

while True:     # 
    cmd = buttonbox("请选择","当当成绩管理系统",("查看成绩","修改成绩","退出"))
    
    if cmd == "退出":
        msgbox("退出成功！")
        break
    
    elif cmd == "查看成绩":
        with open("file.txt") as file:
            cj = file.read()
            msgbox(cj)
    elif cmd == "修改成绩":
        cj = textbox("请输入成绩")
        with open("file.txt","w") as file:
            file.write(cj)
        msgbox("修改成功！")