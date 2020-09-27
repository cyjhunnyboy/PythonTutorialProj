"""
什么是字符串？
    字符串是以单引号或者双引号括起来的任意文本
    如：'abc', "define"

注意：字符串不可变

"""
# 创建字符串
str1 = "Sunny is a good man!"
str2 = "Tom is a nice man!"
str3 = "John is a handsome man!"

"""
字符串运算
"""
# 字符串连接
strA = "Tom is a "
strB = "good man!"
strC = strA + strB
print("strC = ", strC)
print("strA = ", strA)
print("strB = ", strB)

# 输出重复字符串
strD = "good"
print("strD 输出3次：", strD * 3)

# 访问字符串中的某一个字符
# 通过索引下标查找字符，索引从0开始
strE = "Tom is a good man!"
print("strE[1] = ", strE[1])
# TypeError: 'str' object does not support item assignment
# 字符串不可变
# strE[1] = "a"
print("strE = ", strE)

# 截取字符串中的一部分
strF = "Sunny is a good man!"
# 截取部分的时候，包含初始下标，但不包含末尾下标值
# 因为索引是从0开始的
# 从给定下标处开始截取到给定下标结束之前
strG = strF[6:15]
strH = strF[0:6]
# 从头截取到给定下标之前的字符
strI = strF[:6]
# 从给定下标处开始截取到结尾
strJ = strF[16:]
strK = strF[:]
print("strG = ", strG)
print("strH = ", strH)
print("strI = ", strI)
print("strJ = ", strJ)
print("strK = ", strK)

strAA = "sunny is a good man!"
print("good" in strAA)
print("nice" not in strAA)

# 00000101
# 11111010  补码
# 10000101  反码（除符号位外，按位取反）
# 10000110  原码（反码+1） = -6
print(~5)


"""
eval(str)
功能：将字符串str当成有效的表达式来求值并返回计算结果
"""
numA = eval("123")
print("numA = ", numA)
print(type(numA))
print(eval("+123"))
print(eval("-123"))
print(eval("12+3"))
print(eval("12-3"))
# print(eval("12a3"))
# print(eval("a123"))

"""
len(str)
功能：返回str字符串的长度（字符个数）
"""
print(len("sunny is a good man!"))

"""
str.lower()
功能：将str字符串中大写字母转换为小写字母
"""
numB = "SUNNY is a good man!凯"
print(numB.lower())
# numB 没有改变，numB.lower()重新生成全部为小写字符串并返回该字符串
print("numB = %s" % numB)

"""
str.upper()
功能：将str字符串中小写字母转换为大写字母
"""
numC = "SUNNY is a good man!凯"
print(numB.upper())
# numC 没有改变，numC.lower()重新生成全部为大写写字符串并返回该字符串
print("numC = %s" % numC)


"""
swapcase()
功能：转换字符串中大写字母为小写字母，小写字母为大写字母，并返回该新的字符串，原字符串不变
"""
numD = "SUNNY is a Good Man!"
print(numD.swapcase())
print("numD = %s" % numD)

"""
str.capitalize()
功能：字符串首字母大写，其他字符转为小写，即书信格式
"""
numE = "SUNNY is a Good MAN!"
print(numE.capitalize())
print("numE = %s" % numE)

"""
str.title()
功能：每个单词的首字母大写，其他字母小写
"""
numF = "SUNNY is a gOOd MaN!"
print(numF.title())
print("numF = %s" % numF)

"""
str.center(width, fillChar)
width: 字符串宽度
fillChar: 填充字符, 默认空格填充
功能：返回一个指定宽度的居中的字符串
"""
numG = "Kaige is a nice man!"
print(numG.center(40, "*"))
print("numG = %s" % numG)

"""
str.ljust(width[,fillChar])
width: 字符串宽度
fillChar: 填充字符，默认空格填充
功能：返回一个指定宽度的居左的字符串
"""
numI = "Kaige is a good man!"
print(numI.ljust(40), "*")
print(numI.ljust(40, "*"))
print("numI = %s" % numI)


"""
str.rjust(width[,fillChar])
width: 字符串宽度
fillChar: 填充字符，默认空格填充
功能：返回一个指定宽度的居右的字符串
"""
print(numI.rjust(40))
print(numI.rjust(40, "*"))
print("numI = %s" % numI)

"""
str.zfill(with)
width: 字符串宽度
功能：返回一个长度为width的字符串，原字符串右对齐，前面补零
"""
print(numI.zfill(40))
print("numI = %s" % numI)

"""
count(str[,start][,end])
功能：返回字符串中str出现的次数
"""
numJ = "sunny is a good good man!"
print("numJ = %s" % numJ)
print("good 字符串出现的次数为：%d" % numJ.count("good"))
print(numJ.count("good", 15, len(numJ)))

"""
find(str[,start][,end])
功能：从左向右检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾，返回str第一次出现的开始下标，没有返回-1
"""
str11 = "Sunny is a very very good man!"
print(str11.find("very"))
print(str11.find("hello"))
print(str11.find("very", 15, len(str11)))

"""
rfind(str[,start][,end])
功能：从右向左检测str字符串是否包含在字符串中，可以指定范围，默认从头到尾，返回str第一次出现的开始下标，没有返回-1
"""
str12 = "Sunny is a very very good man!"
print(str12.rfind("very"))
print(str12.rfind("hello"))
print(str12.rfind("very", 0, 15))

"""
index(str, start=0, end=len(str))
和find方法一样，只不过如果str不存在的时候会抱一个异常
"""
str13 = "Sunny is a good man!"
print(str13.index("good"))
# ValueError: substring not found
# print(str13.index("hello"))

"""
rindex(str, start=0, end=len(str))
和rfind方法一样，只不过如果str不存在的时候会抱一个异常
"""
str14 = "kaige is a very very nice man!"
print(str14.rindex("very"))
# ValueError: substring not found
# print(str14.rindex("hello"))

"""
lstrip()
截掉字符串左侧指定的字符，默认为空格
"""
str15 = "*********kaige is a very very nice man! "
print(str15.lstrip("*"))
print("str15 = %s" % str15)


"""
rstrip()
截掉字符串右侧指定的字符，默认为空格
"""
str16 = "^^^^^^^^^kaige is a very very nice man!^^^^^^^^^^^"
print(str16.rstrip("^"))
print("str16 = %s" % str16)


"""
strip()
截掉字符串左右两侧指定的字符，默认为空格
"""
str17 = "^^^^^^^^^kaige is a very very nice man!^^^^^^^^^^^"
print(str17.strip("^"))
print("str17 = %s" % str17)


str18 = "a"
print(ord(str18))
str19 = chr(65)
print(str19)

print("a" == "a")
print(" " == " ")
