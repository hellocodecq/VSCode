"""
    当当日记
    1. 当当安全防御: 通过指定filename打开文件
    2. 完善框架: while True
    3. 实现基础功能: 查看日记、写日记、退出
    4. 实现功能: 销毁日记, w模式打开，直接pass
    5. 实现功能: 密码，修改文件第一行储存密码，则删除的时候需要把密码写入 
    6. 实现功能: 使用密码登录，保存密码于变量code中，打开文件后输入密码验证
    7. 完善功能: 查看日记不显示密码
    ---
    家庭作业: 
    1. 销毁日记需要密码确认
    2. 添加功能: 查看密码  
    ---
    拓展: 
    1. 修改密码（难度比较大）
"""
from easygui import *

filename = enterbox(msg="请输入日记本名",title="当当安全防御")
code = None

try:
    with open(filename, encoding="utf-8") as file:
        pswd = passwordbox(msg="请输入日记本密码",title="当当安全防御")
        code = file.readlines()[0].strip()
        if pswd == code:
            msgbox("登录成功！")
        else:
            msgbox("密码错误！")
            exit(1)
except FileNotFoundError:
    msgbox("错误！没有这本日记！")
    exit(1)



while True:
    cmd = buttonbox(msg="请选择功能",title="当当日记",choices=("查看日记","查看密码","写日记","销毁日记","退出"))
    if cmd=="查看日记":
        with open(filename, encoding="utf-8") as file:
            file.readline()
            msgbox(title="当当日记",msg=file.read())

    elif cmd == "查看密码":             # 家庭作业
        msgbox("密码: "+code)           # 家庭作业

    elif cmd == "写日记":
        with open(filename, "a",encoding="utf-8") as file:
                text = textbox(msg="请输入日记内容: ",title="写日记")
                file.write("\n"+text+"\n")

    elif cmd == "销毁日记":
        sure = buttonbox(msg="你确定？",title="销毁日记", choices=("是的","我手滑了"))
        if sure == "是的":
            pswd = passwordbox("请输入密码: ","销毁确认") # 家庭作业
            if pswd == code:                            # 家庭作业
                with open(filename,"w") as file:
                    file.write(code)
                msgbox(msg="销毁成功!",title="销毁日记")
            else:
                msgbox("密码不正确！")
        else:
            msgbox(msg="一定要注意安全！",title="别手滑了")

    elif cmd == "退出":
        msgbox("退出成功！")
        break

