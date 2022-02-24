# 主窗口

import tkinter as tk

import subPage as sp

main_window = tk.Tk()

main_window.title ("给当当同学的TK")

main_window.geometry('800x600')

# set icon
# main_window.iconbitmap("postion")

# 标题
text = tk.Label(main_window, text="显示内容",font=("微软雅黑",50))
text.pack()

# 退出按钮
quit = tk.Button(main_window,text="退出", command=main_window.quit)
quit.pack(side="bottom")

# 开启子窗口
sub = tk.Button(main_window, command=sp.sub_page, text="开启子窗口")
sub.pack()


main_window.mainloop()