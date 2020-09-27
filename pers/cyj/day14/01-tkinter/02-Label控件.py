import tkinter


# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("银行自动提款机系统")
# 设置大小和位置
win.geometry("800x600+400+200")

"""
Label: 标签控件，可以显示文本
win: 主窗体
text: 显示的文本内容
bg: 背景色
fg: 字体颜色
font:字体，元组格式
width: 宽
height：高
wraplength:指定text文本中多宽进行换行
justify: 设置换行后的对齐方式
anchor: 位置（n-北，e-东，s-南，w-西，center-居中，ne-东北，se-东南，sw-西南，nw-西北)，默认center
"""
text = "Sunny is a good man"
label = tkinter.Label(win, text=text, bg="pink", fg="red", font=("Consolas", 20), width=30, height=2)
# 显示出来
label.pack()



win.mainloop()