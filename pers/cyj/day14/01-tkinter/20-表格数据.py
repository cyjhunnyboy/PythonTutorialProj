import tkinter
from tkinter import ttk

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("表格数据")
# 设置大小和位置
win.geometry("800x600+400+200")

# 表格
grid = ttk.Treeview(win)
grid.pack()

# 定义列
grid["columns"] = ("name", "age", "height", "weight")
# 设置列，此时列还不显示
grid.column("name", width=100)
grid.column("age", width=100)
grid.column("height", width=100)
grid.column("weight", width=100)
# 设置表头
grid.heading("name", text="姓名")
grid.heading("age", text="年龄")
grid.heading("height", text="身高")
grid.heading("weight", text="体重")

# 添加数据
grid.insert("", 0, text="1", values=("Tom", "18", "160", "70"))
grid.insert("", 1, text="2", values=("Sunny", "20", "170", "75"))
grid.insert("", 2, text="3", values=("Smith", "22", "180", "80"))
grid.insert("", 3, text="4", values=("John", "19", "165", "70"))

win.mainloop()
