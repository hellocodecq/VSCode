# 淼淼日记

from easygui import *
name = enterbox(msg="请输入要打开的日记本", title="淼淼安全防御")

pswd = ""   # 保存密码

try:
    with open( name ) as file:
        lines = file.readlines()
        pswd = passwordbox(msg="请输入密码",title="淼淼安全防御")
        
        if pswd == lines[0].strip():
            msgbox("验证成功！")
        else:
            msgbox("验证失败！")
            exit()

except Exception as e:
    print(e)
    msgbox("你输入了错误的日记本的名字", ok_button='请你离开')
    exit()

while True:

    cmd = buttonbox(msg="请选择功能", title="日记本",\
            choices=('写日记','读日记','销毁日记','退出'))
    
    print(cmd)  # 显示选择的按钮

    if cmd == '退出':
        break
    
    elif cmd == '读日记':
        with open( name) as file:
            file.readline()         # 读取一行
            msgbox(file.read())

    elif cmd=='写日记':
        with open(name, 'a') as file:
            text = textbox(msg='请输入',title='写日记')
            file.write(text+"\n")
    
    elif cmd=='销毁日记':
        with open(name, 'w') as file:   # 清空文件
            file.write(pswd+"\n")   # 再把密码写进去
        
        msgbox("清空完毕！")
