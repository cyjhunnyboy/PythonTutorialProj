# 从控制台输入一个字符串，返回这个字符串中有多少个单词
str = input("请输入字符串：")
str = str.strip()
index = 0
count = 0
# sunny is    a good   man
while index < len(str):
    while str[index] != " ":
        index += 1
        if index == len(str):
            # 结束整个循环
            break
    count += 1
    if index == len(str):
        break
    while str[index] == " ":
        index += 1
print("str = %s 的单词个数是 %d" % (str, count))
