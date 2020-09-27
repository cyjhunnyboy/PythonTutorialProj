import os

# 读文件的一个完整过程
path = os.path.abspath(".") + "\\file1.txt"

# 最佳方式
with open(path, "r", encoding="utf-8", errors="ignore") as f2:
    print(f2.read())
    print("===========================")
