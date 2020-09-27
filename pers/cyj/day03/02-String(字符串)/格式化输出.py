"""
格式化输出
"""
num = 10
str = "sunny is a good man!"
f = 10.123456789
# %d %s %f 占位符
print("num = %d" % num)
print("num = ", num, "str = ", str)
print("num = %d, str = %s" % (num, str))
print("num = %d, str = %s, f = %f" % (num, str, f))
# 精确到小数点后3位，会四舍五入
print("num = %d, str = %s, f = %.3f" % (num, str, f))
print("num = %d, str = %s, f = %.4f" % (num, str, f))
print("num = %d, str = %s, f = %.5f" % (num, str, f))
print("num = %d, str = %s, f = %.6f" % (num, str, f))
print("num = %d, str = %s, f = %.7f" % (num, str, f))
print("num = %d, str = %s, f = %.8f" % (num, str, f))
"""
转义字符 \
将一些字符转换成有特殊意义的字符
"""
# 常用的转义字符：\n--换行，
print("num = %d\nstr = %s\nf = %.3f" % (num, str, f))
print("sunny \\n is a good man!")
print("Tom is a \'good\' man!")
# 如果字符串内有很多换行，用\n写在一行不好阅读
print("good\nnice\nhandsome")
print('''
good
nice
handsome

''')

"""
\t 制表符
"""
print("对面的女孩\t看过来！")

# 打印 |||t|||
print(r"|||t|||")
# 打印 \\\t\\
# 如果字符中有好多字符串都需要转义，就需要加入好多\，为了简化，Python允许用r表示内部的字符串默认不转义
print(r"\\\t\\")
print(r"E:\Code\Python\经典Python教程入门到精通\PythonTutorialProj\tday03")
print(r"/root/usr/sunck/Desktop/Python3.8/day03")
