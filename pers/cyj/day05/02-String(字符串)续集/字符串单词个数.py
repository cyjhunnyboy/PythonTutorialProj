# 从控制台输入一个字符串，返回这个字符串中有多少个单词
str = input("请你输入字符串：")
list_str = str.split(" ")
count = 0
for s in list_str:
    if len(s) > 0:
        count += 1
print("您输入字符串\"%s\"的单词个数是：%d" % (str, count))
