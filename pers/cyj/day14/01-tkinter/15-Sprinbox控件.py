import tkinter


def update():
    print(sprinVar.get())

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("Spinbox控件")
# 设置大小和位置
win.geometry("800x600+400+200")

# 绑定变量
sprinVar = tkinter.StringVar()

"""
数值范围控件
"""
# increment 步长，默认为1
# values 最好不要与from=0, to=100, increment=10同时使用
# spinbox = tkinter.Spinbox(win, values=(0, 2, 4, 6, 8))
# command 只要值改变就会执行对应的方法
spinbox = tkinter.Spinbox(win, from_=0, to=100, increment=10, textvariable=sprinVar, command=update)
spinbox.pack()

# 赋值
sprinVar.set(20)
# 取值
print(sprinVar.get())


win.mainloop()
