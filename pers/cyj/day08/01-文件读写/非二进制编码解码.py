import os

path = os.path.abspath(".") + "\\files\\b.txt"

"""
文件读写应编码格式一致
"""

# 写文件
# 编码
with open(path, "w", encoding="utf-8") as fWrite:
    str = "Sunny is a good man凯"
    fWrite.write(str)


# 读文件
# 解码
# with open(path, "r") as fRead:
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 21: incomplete multibyte sequence
# with open(path, "r", errors="ignore") as fRead:
# Sunny is a good man鍑 <class 'str'>
with open(path, "r", encoding="utf-8") as fRead:
    data = fRead.read()
    # Sunny is a good man凯 <class 'str'>
    print(data, type(data))
