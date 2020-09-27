import os

# 读文件的一个完整过程
path = os.path.abspath(".") + "\\file1.txt"
try:
    f = open(path, "r", encoding="utf-8", errors="ignore")
    print("===========================")
    print(f.read())
    print("===========================")
except FileNotFoundError as e:
    print("文件不存在！")
finally:
    if f:
        f.close()



# 最佳方式
with open(path, "r", encoding="utf-8", errors="ignore") as f2:
    print(f2.read())
    print("===========================")
