import tkinter


def update():
    print(r.get())

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("单选框控件：RadioButton")
# 设置大小和位置
win.geometry("800x600+400+200")

# 绑定变量
# 一组单选框要绑定同一变量
r = tkinter.IntVar()

# 单选框控件
radio1 = tkinter.Radiobutton(win, text="money", value=1, variable=r, command=update)
radio1.pack()
radio2 = tkinter.Radiobutton(win, text="power", value=2, variable=r, command=update)
radio2.pack()
radio3 = tkinter.Radiobutton(win, text="people", value=3, variable=r, command=update)
radio3.pack()

win.mainloop()
