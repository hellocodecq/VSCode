import tkinter as tk
import time
import threading

from easygui import buttonbox, enterbox, msgbox

def start_count(minite):
    print("开始计时")
    count_window = tk.Tk()
    count_window.title("计时中")
    time_now = minite
    label = tk.Label(count_window, text=str(time_now))
    label.pack()

    
    count_window.mainloop()


def sub_page():
    sub_window = tk.Tk()
    sub_window.title("输入时间")
    sub_window.geometry('400x200')
    label = tk.Label(sub_window,text="请输入分钟数：")

    def check():
        try:
            num = int(enter.get())
            sub_window.destroy()
            return start_count(num)
        except:
            print("非数字")
            msgbox("请输入数字")

    enter = tk.Spinbox(sub_window,from_=1, to=300,increment=1)
    button = tk.Button(sub_window, text="确认", command=check)
    label.pack()
    enter.pack()
    button.pack()

    sub_window.mainloop()

if __name__ == '__main__':
    print(sub_page())