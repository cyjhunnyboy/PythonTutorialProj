import tkinter
from tkinter import ttk


def func(event):
    print(combobox.get())
    print(comboboxVar.get())

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("银行自动提款机系统")
# 设置大小和位置
win.geometry("800x600+400+200")

# 绑定变量
comboboxVar = tkinter.StringVar()

# 添加下拉控件
combobox = ttk.Combobox(win, textvariable=comboboxVar)
combobox.pack()

# 设置下拉数据
combobox["value"] = ("黑龙江", "吉林", "辽宁")

# 设置默认值
combobox.current(0)

# 绑定事件
combobox.bind("<<ComboboxSelected>>", func)

win.mainloop()
