import tkinter


def myPrint(event):
    # print(listbox.curselection())
    print(listbox.get(listbox.curselection()))

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("列表控件：Listbox")
# 设置大小和位置
win.geometry("800x600+400+200")

# 绑定变量
lbv = tkinter.StringVar()

# 与BROWSE相似，但是不支持鼠标按下后移动选中位置
listbox = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
listbox.pack()
for item in ["vg", "vn", "vk", "good", "nice", "handsome", "cool"]:
    # 按顺序添加
    listbox.insert(tkinter.END, item)

# 打印当前列表中的选项
# print(lbv.get())

# 设置选项
# lbv.set(("1", "2", "3"))

# 绑定事件
# Double-Button-1: 双击鼠标左键
listbox.bind("<Double-Button-1>", myPrint)

win.mainloop()
