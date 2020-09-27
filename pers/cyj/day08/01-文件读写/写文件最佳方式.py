import os

path = os.path.abspath(".") + "\\files\\file6.txt"

# 写文件最佳方式
with open(path, "a", encoding="utf-8") as f2:
    f2.write("Sunny is a good man!\n")
