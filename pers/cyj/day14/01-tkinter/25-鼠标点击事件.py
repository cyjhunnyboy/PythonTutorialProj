import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("鼠标点击事件")
# 设置大小和位置
win.geometry("800x600+400+200")

def func(event):
    print(event.x, event.y)

# Label也可以触发鼠标点击事件
# lable1 = tkinter.Label(win, text="leftmouse button")
button1 = tkinter.Button(win, text="leftmouse button")
# <Button-1> 鼠标左键
# <Button-2> 鼠标中键
# <Button-3> 鼠标右键
# <Double-Button-1> 鼠标左键双击
# <Double-Button-2> 鼠标中键双击
# <Triple-Button-1> 鼠标左键三击
# bind 给控件绑定事件
# button1.bind("<Button-1>", func)
# button1.bind("<Double-Button-1>", func)
button1.bind("<Triple-Button-1>", func)
button1.pack()


win.mainloop()
