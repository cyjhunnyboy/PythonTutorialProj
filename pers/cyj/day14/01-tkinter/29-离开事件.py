import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("离开事件")
# 设置大小和位置
win.geometry("800x600+400+200")

label = tkinter.Label(win, text="Sunny is a good man", bg="pink")
label.pack()

def func(event):
    print(event.x, event.y)

# <Leave> 鼠标光标离开时控件时触发
label.bind("<Leave>", func)

win.mainloop()
