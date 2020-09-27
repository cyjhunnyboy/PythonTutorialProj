"""
打印出所有三位数中的水仙花数
告诉我五位数中有多少个回文数
从控制台输入一个数，判断是否是质数
从控制台输入一个数，分解质因数
从控制台输入一个字符串，返回这个字符串中有多少个单词
从控制台输入一个字符串，打印出这个字符串中所有数字字符的和
"""
# 打印出所有三位数中的水仙花数
num = 100
while num <= 999:
    a = num % 10
    b = num // 10 % 10
    c = num // 100
    if num == a ** 3 + b ** 3 + c ** 3:
        print("%d 是水仙花数" % num)
    num += 1


# 告诉我五位数中有多少个回文数
print("=============================")
num = 10000
sum = 0
while num <= 99999:
    a = num % 10
    b = num // 10000
    c = num // 10 % 10
    d = num // 1000 % 10
    if a == b and c == d:
        print("num = %d" % num)
        sum += 1
        num += 1
    else:
        num += 1
print("五位数中有%d个回文数" % sum)


# 从控制台输入一个数，判断是否是质数
print("=============================")
num = int(input("请您输入一个数："))
if num == 2:
    print("%d是质数" % num)
index = 2
flag = False
while index < num:
    if num % index == 0:
        flag = True
        index += 1
    else:
        index += 1

if flag is False:
    print("%d是质数" % num)
else:
    print("%d不是质数" % num)


# 从控制台输入一个字符串，打印出这个字符串中所有数字字符的和
print("=============================")
str = input("请输入一串包含数字的字符串：")
index = 0
sum = 0
while index < len(str):
    if "0" <= str[index] <= "9":
        sum += int(str[index])
    index += 1
print("sum = %d" % sum)

# 字符串比较大小
# 从第一个字符开始比较，谁的ASCII值大谁就大，如果相等会比较下一个字符的ASCII值大小，那么谁的值大谁就大
print("baaaaa" < "caaaaa")

