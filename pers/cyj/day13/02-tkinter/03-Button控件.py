import tkinter


def func():
    print("Sunny is a good man!")


# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("银行自动提款机系统")
# 设置大小和位置
win.geometry("800x600+400+200")

# 创建按钮
button1 = tkinter.Button(win, text="按钮1", command=func, width=10, height=2)
# 显示按钮
button1.pack()

# 创建按钮
button2 = tkinter.Button(win, text="按钮2", command=lambda: print("Sunny is a good man!"), width=10, height=2)
# 显示按钮
button2.pack()

# 创建按钮
button3 = tkinter.Button(win, text="按钮3", command=win.quit, width=10, height=2)
# 显示按钮
button3.pack()

win.mainloop()
