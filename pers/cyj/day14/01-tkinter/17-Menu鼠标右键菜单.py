import tkinter


def showMenu(event):
    menu.post(event.x_root, event.y_root)


# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("Menu鼠标右键菜单")
# 设置大小和位置
win.geometry("800x600+400+200")

# 菜单条
menubar = tkinter.Menu(win)

# 添加菜单
menu = tkinter.Menu(menubar, tearoff=False)
for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell", "Java", "JS", "PHP", "汇编", "NodeJS", "退出"]:
    menu.add_command(label=item)
# 将菜单添加到菜单条
menubar.add_cascade(label="语言", menu=menu)

# 绑定鼠标右键事件
win.bind("<Button-3>", showMenu)

win.mainloop()
