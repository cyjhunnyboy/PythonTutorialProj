import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("银行自动提款机系统")
# 设置大小和位置
win.geometry("800x600+400+200")

"""
输入控件：用于显示简单的文本内容
show: 密文显示，“*”表示输入内容以星号显示
"""
# 绑定变量
e = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=e)
entry.pack()
# e就代表输入框这个对象
# 设置值
e.set("Sunny is a good man!")
# 取值方式
print(e.get())
print(entry.get())

win.mainloop()
