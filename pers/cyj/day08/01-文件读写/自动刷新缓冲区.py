import os
import time

path = os.path.abspath(".") + "\\files\\file4.txt"


"""
1、打开文件
"""
f = open(path, "w", encoding="utf-8", errors="ignore")


"""
2、写入文件
"""
# 缓冲区满后，自动刷新缓冲区
# 死循环，不执行后面关闭文件操作
while 1:
    f.write("Sunny is a good man!")
    time.sleep(0.01)


"""
3、关闭文件
"""
f.close()