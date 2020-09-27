import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("框架控件: Frame")
# 设置大小和位置
win.geometry("800x600+400+200")

"""
框架控件：在屏幕上显示一个矩形区域，多作为容器控件
"""
frame = tkinter.Frame(win)
frame.pack()

# left frame
leftFrame = tkinter.Frame(frame)
tkinter.Label(leftFrame, text="左上", bg="pink").pack(side=tkinter.TOP)
tkinter.Label(leftFrame, text="左下", bg="blue").pack(side=tkinter.TOP)
leftFrame.pack(side=tkinter.LEFT)

# right frame
rightFrame = tkinter.Frame(frame)
tkinter.Label(rightFrame, text="右上", bg="red").pack(side=tkinter.TOP)
tkinter.Label(rightFrame, text="右下", bg="yellow").pack(side=tkinter.TOP)
rightFrame.pack(side=tkinter.RIGHT)

win.mainloop()
