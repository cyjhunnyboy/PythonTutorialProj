import os

path = os.path.abspath(".") + "\\files\\file5.txt"

# 写文件完整过程
try:
    f = open(path, "w", encoding="utf-8", errors="ignore")
    f.write("Sunny is a good man!")
except FileNotFoundError as e:
    print("文件不存在！")
finally:
    if f:
        f.close()


# 写文件最佳方式
with open(path, "w", encoding="utf-8") as f2:
    f.write("Sunny is a good man!")
