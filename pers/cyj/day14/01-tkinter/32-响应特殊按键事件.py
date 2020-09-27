import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("响应特殊按键的事件")
# 设置大小和位置
win.geometry("800x600+400+200")

label = tkinter.Label(win, text="Sunny is a good man", bg="pink")
# 设置焦点
label.focus_set()
label.pack()

def func(event):
    print("event char = '%s'" % event.char)
    print("event keycode = '%s'" % event.keycode)

# <Shift_L> 左shift
# <Shift_R> 右shift
# <F5>
# <Return> 回车
# <BackSpace> 退格
label.bind("<Shift_L>", func)


win.mainloop()
