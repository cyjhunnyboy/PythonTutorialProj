import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("列表控件：Listbox")
# 设置大小和位置
win.geometry("184x200+500+300")

# MULTIPLE，支持多选
listbox = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
for item in ["vg", "vn", "vk", "good", "nice", "handsome", "cool",
             "vg2", "vn2", "vk2", "good2", "nice2", "handsome2", "cool2",
             "vg3", "vn3", "vk3", "good3", "nice3", "handsome3", "cool3"]:
    # 按顺序添加
    listbox.insert(tkinter.END, item)

# 滚动条
scroll = tkinter.Scrollbar(win)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox.configure(yscrollcommand=scroll.set)
listbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
scroll["command"] = listbox.yview


win.mainloop()
