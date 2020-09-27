import os

path = os.path.abspath(".") + "\\files\\file3.txt"

"""
1、打开文件
"""
# f = open(path, "w")
# f = open(path, "w", encoding="utf8")
f = open(path, "w", encoding="utf-8", errors="ignore")


"""
2、写文件
"""
# 1、将信息写入缓冲区
f.write("Sunny is a goood man!")
# 2、刷新缓冲区
# 直接把内部缓冲区的数据立刻写入文件，而不是被动的等待自动刷新缓冲区写入
# 刷新缓冲区方式：1、关闭文件；2、手动刷新；3、缓冲区满了；4、遇到\n
f.flush()

# while True:
#     pass

"""
3、关闭文件
"""
f.close()
