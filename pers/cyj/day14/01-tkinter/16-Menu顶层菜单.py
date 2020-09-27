import tkinter


def func():
    print("Sunny is a good man!")

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("Menu顶层菜单")
# 设置大小和位置
win.geometry("800x600+400+200")

# 菜单条
menubar = tkinter.Menu(win)
win.configure(menu=menubar)

# 创建第一个菜单选项：语言
menu1 = tkinter.Menu(menubar, tearoff=False)
# 给第一个菜单选项添加内容
for item in ["Python", "Java", "Perl", "C", "C++", "Swift", "C#", "PHP", "JS", "NodeJS", "退出"]:
    if item == "退出":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(label=item, command=func)
# 向菜单条上添加“语言”菜单选项
menubar.add_cascade(label="语言", menu=menu1)

# 创建第二个菜单选项：颜色
menu2 = tkinter.Menu(menubar, tearoff=False)
# 给第二个菜单选项添加内容
menu2.add_command(label="red")
menu2.add_command(label="blue")
menu2.add_command(label="green")
menu2.add_command(label="black")
# 向菜单条上添加“颜色”菜单选项
menubar.add_cascade(label="颜色", menu=menu2)


win.mainloop()
