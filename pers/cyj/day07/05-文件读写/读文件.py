import os

"""
过程：
1、打开文件
2、读文件内容
3、关闭文件

打开文件：
1、open(path, flag[, encoding][,errors])
    path: 要打开文件的路径
    flag: 打开方式
        r           以只读的方式打开文件，文件的描述符放在文件的开头
        rb          以二进制格式打开一个文件用于只读，文件的描述符放在文件的开头
        r+          打开一个文件用于读写，文件的描述符放在文件的开头
        w           打开一个文件只用于写入，如果该文件已经存在会覆盖，不存在则创建新文件
        wb          打开一个文件只用于写入二进制，如果该文件已经存在会覆盖，不存在则创建新文件
        w+          打开一个文件用于读写
        a           打开一个文件用于追加，如果文件存在，文件描述符将会放到文件末尾
        a+          打开一个文件用于读写，在文件末尾写入
    encoding: 编码方式
    errors: 错误处理
"""

"""
1、打开文件
"""
path = os.path.abspath(".") + "\\file1.txt"
# f = open(path, "r")
# f = open(path, "r", encoding="utf8")
# f = open(path, "r", encoding="utf-8")
f = open(path, "r", encoding="utf-8", errors="ignore")

"""
2、读文件内容
"""
# 1、读取文件全部内容
str1 = f.read()
print("*" + str1 + "*")
print("=======================")

# 2、读取指定字符数
# 修改描述符的位置
f.seek(0)
str2 = f.read(21)
print("*" + str2 + "*")
print("=======================")

# 3、读取整行，包括“\n”字符
# 修改描述符的位置
f.seek(0)
str3 = f.readline()
print("*" + str3 + "*")
print("=======================")

# 4、读取指定字符数
# 修改描述符的位置
f.seek(0)
str4 = f.readline(21)
print("*" + str4 + "*")
print("=======================")

# 5、读取所有行并返回列表（包括换行符）
# 修改描述符的位置
f.seek(0)
list = f.readlines()
print(list)
print("=======================")

# 6、若给定的数字大于0，返回实际size字节的行数
# 修改描述符的位置
f.seek(0)
list2 = f.readlines(22)
print(list2)
print("=======================")

# 修改描述符的位置
f.seek(0)
str5 = f.read()
print(str5)

"""
3、关闭文件
"""
f.close()
