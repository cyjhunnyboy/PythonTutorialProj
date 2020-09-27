import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("列表框控件：Listbox")
# 设置大小和位置
win.geometry("800x600+400+200")

"""
列表框控件，可以包含一个或者多个文本框
作用：在listbox控件的小窗口显示一个字符串
"""
# 1、创建一个listbox，添加几个元素
listbox = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
listbox.pack()
for item in ["vg", "vn", "vk", "good", "nice", "handsome", "cool"]:
    # 按顺序添加
    listbox.insert(tkinter.END, item)
# 在开始添加
listbox.insert(tkinter.ACTIVE, "great")
# 在结尾添加
listbox.insert(tkinter.END, "bad")
# 将列表当成一个元素添加
# listbox.insert(tkinter.END, ["very good", "very nice"])

# 删除，参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只删除第一个索引处的内容
listbox.delete(1, 3)
# listbox.delete(1)

# 选中，参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只选中第一个索引处的内容，索引是从0开始
# listbox.select_set(0, 3)
listbox.select_set(2, 4)

# 取消选中，参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只取消选中第一个索引处的内容，索引是从0开始
listbox.select_clear(3)

# 获取到列表中的元素格式
print(listbox.size())

# 从列表中取值, 参数1为开始的索引，参数2为结束的索引，如果不指定参数2，只获取第一个索引处的内容，索引是从0开始
print(listbox.get(2, 4))
# print(listbox.get(2))

# 返回当前的索引项，不是item元素
print(listbox.curselection())

# 判断一个选项是否被选中
print(listbox.select_includes(2))
print(listbox.select_includes(0))


win.mainloop()
