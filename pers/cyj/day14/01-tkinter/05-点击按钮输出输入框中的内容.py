import tkinter


def showInfo():
    print(entry.get())


# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("银行自动提款机系统")
# 设置大小和位置
win.geometry("800x600+400+200")

# 输入框
entry = tkinter.Entry(win)
entry.pack()
# 按钮
button = tkinter.Button(win, text="按钮", command=showInfo)
button.pack()

win.mainloop()
