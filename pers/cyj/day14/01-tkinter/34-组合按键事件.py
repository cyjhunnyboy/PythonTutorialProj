import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("组合按键事件")
# 设置大小和位置
win.geometry("800x600+400+200")

def func(event):
    print("event char = '%s'" % event.char)
    print("event keycode = '%s'" % event.keycode)

# <Control-Alt-b>
# <Shift-Up>
win.bind("<Control-Alt-b>", func)


win.mainloop()
