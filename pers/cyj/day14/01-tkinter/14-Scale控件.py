import tkinter


# 取值
def showNum():
    print(scale1.get())


# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("Scale控件")
# 设置大小和位置
win.geometry("800x600+400+200")

"""
供用户拖拽指示器改变变量的值，可水平，也可以垂直
tkinter.HORIZONTAL 水平
tkinter.VERTICAL 垂直（默认）
length: 水平时表示宽度，垂直时表示高度
tickinterval 选择值将会为该值的倍数
"""
scale1 = tkinter.Scale(win, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=100, length=200)
scale1.pack()

tkinter.Button(win, text="按钮", command=showNum).pack()

# 设置值
scale1.set(20)

win.mainloop()
