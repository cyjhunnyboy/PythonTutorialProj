import os

# 编码
path = os.path.abspath(".") + "\\files\\a.txt"

"""
以二进制读写文件，写文件内容必须要进行编码，读文件编码方式必须和写入一致
"""

# with open(path, "wb", encoding="uft-8") as fWrite:
# ValueError: binary mode doesn't take an encoding argument
with open(path, "wb") as fWrite:
    str = "Sunny is a good man凯"
    fWrite.write(str.encode("utf-8"))


# 解码
# ValueError: binary mode doesn't take an encoding argument
# with open(path, "rb", encoding="utf-8") as fRead:
with open(path, "rb") as fRead:

    data = fRead.read()

    # 写入时“Sunny is a good man”不含中文，以二进制方式进行写入，且编码为“utf-8”
    # 读取时，未进行编码为“utf-8”，读取出来的内容会带二进制标识符
    # “b'Sunny is a good man' <class 'bytes'>”
    # print(data, type(data))

    # 写入时“Sunny is a good man凯”含中文，且编码为“utf-8"
    # 读取时，未进行解码为“utf-8”，会出现中文乱码
    # b'Sunny is a good man\xe5\x87\xaf' <class 'bytes'>
    # print(data, type(data))

    # 写入时“Sunny is a good man凯”含中文，且编码为“utf-8"
    # 读取时，编码为“gbk”，与写入时编码方式不一致，报错
    # UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 21: incomplete multibyte sequence
    # newData = data.decode("gbk")
    # print(newData, type(newData))

    # 写入时“Sunny is a good man凯”含中文，且编码为“utf-8"
    # 读取时，编码为“gbk”，与写入时编码方式不一致，但忽略错误
    # 读取到内容会出现中文乱码，读取数据与写入不一致，Sunny is a good man鍑 <class 'str'>
    # newData = data.decode("gbk", errors="ignore")
    # print(newData, type(newData))

    # 写入时“Sunny is a good man凯”含中文，且编码为“utf-8"
    # 读取时，编码为“utf-8”，与写入时一致，读取内容正常
    newData = data.decode("utf-8")
    print(newData, type(newData))
