import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("响应所有按键的事件")
# 设置大小和位置
win.geometry("800x600+400+200")

label = tkinter.Label(win, text="Sunny is a good man", bg="pink")
# 设置焦点
label.focus_set()
label.pack()

def func(event):
    print("event char = '%s'" % event.char)
    print("event keycode = '%s'" % event.keycode)

# <Key> 响应所有的按键
label.bind("<Key>", func)


win.mainloop()
