import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("鼠标移动事件")
# 设置大小和位置
win.geometry("800x600+400+200")

# Label控件
label = tkinter.Label(win, text="Sunny is a good man")
label.pack()

def func(event):
    print(event.x, event.y)

# <B1-Motion> 按住鼠标左键且控件上移动
# <B3-Motion> 按住鼠标右键且控件上移动
# <B1-Motion> 按住鼠标中键且控件上移动
label.bind("<B1-Motion>", func)

win.mainloop()
