import tkinter
from tkinter import ttk

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("树状数据")
# 设置大小和位置
win.geometry("800x600+400+200")

treeGrid = ttk.Treeview(win)
treeGrid.pack()

# 添加一级树枝
treeF1 = treeGrid.insert("", 0, "China", text="中国", values=("F1",))
treeF2 = treeGrid.insert("", 1, "America", text="美国", values=("F2",))
treeF3 = treeGrid.insert("", 2, "England", text="英国", values=("F3",))

# 添加二级树枝
treeF1_1 = treeGrid.insert(treeF1, 0, "GuangDong", text="黑龙江", values=("F1_1",))
treeF1_2 = treeGrid.insert(treeF1, 1, "JiangSu", text="江苏", values=("F1_2",))
treeF1_3 = treeGrid.insert(treeF1, 2, "Guangxi", text="广西", values=("F1_3",))

treeF2_1 = treeGrid.insert(treeF2, 0, "Washington", text="华盛顿", values=("F2_1",))
treeF2_2 = treeGrid.insert(treeF2, 1, "California", text="加利福尼亚", values=("F2_2",))
treeF2_3 = treeGrid.insert(treeF2, 2, "Alaska", text="阿拉斯加", values=("F2_3",))

# 添加三级树枝
treeF1_1_1 = treeGrid.insert(treeF1_1, 0, "HaErBin", text="哈尔滨", values=("F1_1_1",))
treeF1_2_1 = treeGrid.insert(treeF1_2, 0, "NanJing", text="南京", values=("F1_2_1",))
treeF1_3_1 = treeGrid.insert(treeF1_3, 0, "NanNing", text="南宁", values=("F1_3_1",))


win.mainloop()
