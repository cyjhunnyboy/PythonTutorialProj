import tkinter


def update():
    message = ""
    if hobby1.get() is True:
        message += "money\n"
    if hobby2.get() is True:
        message += "power\n"
    if hobby3.get() is True:
        message += "people\n"

    # 清除text中的所有内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)


# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("多选框控件: CheckButton")
# 设置大小和位置
win.geometry("400x300+500+300")

# checkButton多选框控件
hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=update)
check1.pack()
hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win, text="power", variable=hobby2, command=update)
check2.pack()
hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win, text="people", variable=hobby3, command=update)
check3.pack()

# text多行文本控件
text = tkinter.Text(win, width=50, height=50)
text.pack()

win.mainloop()
