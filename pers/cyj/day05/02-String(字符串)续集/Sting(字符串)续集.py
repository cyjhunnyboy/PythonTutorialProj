"""
split(str="", num)
功能：以str为分隔符截取字符串，指定num，则仅截取num个字符串
"""
str1 = "Sunny is a good man!"
list_str1 = str1.split(" ")
print(list_str1)
count = 0
for s in list_str1:
    if len(s) > 0:
        count += 1
print("字符串\"%s\"单词的个数是：%d" % (str1, count))

"""
splitlines([keepends]) 按照('\r', '\r\n', '\n') 分隔
keepends = True 会保留换行符
"""
print("==================================")
str2 = """Sunny is a good man!
Tom is a nice man!
John is a handsome man!
very very good!
your are right!
"""
list_str2 = str2.splitlines()
print(list_str2)


"""
str.join(seq)
功能：以指定的字符串分隔符(str)，将seq中的所有元素组合成一个字符串
"""
print("==================================")
str3 = ["Sunny", "is", "a", "good", "man!"]
str4 = " ".join(str3)
print(str4)


"""
max()：字符串在ASCII中最大值
min()：字符串在ASCII中最小值
"""
print("==================================")
str5 = "Sunny is a good man!"
print(max(str5))
print("*" + min(str5) + "*")


"""
replace(oldstr, newstr,count)
用newstr替换oldstr，默认是全部替换，如果指定了count，那么只替换前count个，返回一个替换后的新的字符串，原字符串不变
"""
print("==================================")
str6 = "Sunny is a good good man!"
str7 = str6.replace("good", "nice", 1)
print(str6)
print(str7)


"""
创建一个字符串映射表: str.maketrans(oldstr, newstr)
oldstr：要转换的字符串
newstr：目标字符串
如：str.maketrans("ac", "65")  即：a--6 c--5 一一对应

seq.translate(str)
seq：要替换的字符串序列
str：字符串映射表
返回一个根据映射表替换后的新的字符串，原字符串不变
"""
print("==================================")
str8 = str.maketrans("good", "nice")
str9 = "Sunny is a good good good man!"
str10 = str9.translate(str8)
print(str9)
print(str10)


"""
startswith(str[,start=0][,end=len(str)])
在给定的范围内判断是否以给定的字符串开头，如果没有指定范围，默认整个字符串
"""
print("==================================")
str11 = "Sunny is a good man!"
str12 = str11.startswith("Sunny", 0, 20)
print(str12)


"""
endswith(str[,start=0][,end=len(str)])
在给定的范围内判断是否以给定的字符串结尾，如果没有指定范围，默认整个字符串
"""
print("==================================")
str13 = "Sunny is a good man!"
str14 = str13.endswith("!")
print(str14)


"""
编码
encode(encoding="utf-8", errors="strict")
errors = "ignore"  忽略错误
"""
print("==================================")
str15 = "Sunny is a good man!凯"
str16 = str15.encode("utf-8", "ignore")
print(str15)
print(str16)
print(type(str16))

"""
解码
decode(encoding="utf-8", errors="strict")
errors = "ignore" 忽略错误
注意：要与编码时的编码格式一致
"""
print("==================================")
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 22: incomplete multibyte sequence
# str17 = str16.decode("gbk")
str17 = str16.decode("utf-8", "ignore")
print(str17)
print(type(str17))


"""
isalpha()
如果字符串中至少有一个字符且所有的字符都是字母返回True，否则返回False
"""
print("==================================")
print("Sunnyisagoodman".isalpha())
print("Sunny is a good man!".isalpha())


"""
isalnum()
如果字符串中至少有一个字符且所有的字符都是字母或者数字返回True，否则返回False
"""
print("==================================")
print("123".isalnum())
print("123a".isalnum())
print("123A".isalnum())
print("123A@".isalnum())


"""
isupper()
如果字符串中至少有一个英文字符且所有的英文字符都是大写的英文字母返回True，否则返回False
"""
print("==================================")
print("ABC".isupper())
print("ABcd".isupper())
print("1".isupper())
print("a".isupper())
print("ABC123".isupper())
print("ABC#%1".isupper())


"""
islower()
如果字符串中至少有一个英文字符且所有的英文字符都是小写的英文字母返回True，否则返回False
"""
print("==================================")
print("abc".islower())
print("abC".islower())
print("1".islower())
print("A".islower())
print("abc1".islower())
print("abc#".islower())

"""
isTitle()
如果字符串是标题化的返回True，否则返回False
"""
print("==================================")
print("Sunny Is A Good Man".istitle())
print("Sunny is a good man".istitle())


"""
isdigit()
如果字符串中只包含数字字符返回True，否则返回False
"""
print("==================================")
print("123".isdigit())
print("123a".isdigit())


"""
isnumeric()
如果字符串中只包含数字字符返回True，否则返回False
"""
print("==================================")
print("123".isnumeric())
print("123a".isnumeric())


"""
isdecimal()
字符串中只包含十进制字符返回True，否则False
"""
print("==================================")
print("123".isdecimal())
print("123a".isdecimal())

"""
isspace()
如果字符串中只包含空格则返回True，否则返回False
"""
print("==================================")
print(" ".isspace())
print("     ".isspace())
print("\t".isspace())
print("\n".isspace())
print("\r".isspace())
print("\f".isspace())
