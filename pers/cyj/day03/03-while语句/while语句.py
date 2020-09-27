"""
while 语句:

格式：
while 表达式:
    语句
逻辑：当程序执行到while语句时，首先计算“表达式”的值，如果“表达式”的值为假，那么结束整个while语句。如果“表达式”的值为真，则执行“语句”
执行完“语句”再去计算“表达式”的值，如果“表达式”的值为假，那么结束整个while语句，如果“表达式”的值还为真，则执行“语句”，执行完“语句”再去计算“表达式”
的值。如此循环往复，直到“表达式”的值为假才停止
"""
num = 1
while num <= 5:
    print("num = %d" % num)
    num += 1

# 计算1+2+3+.....+100
print("=====================================")
sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print("sum = %d" % sum)

print("=====================================")
str = "sunny is a handsome man!"
index = 0
while index < len(str):
    if str[index] == " ":
        index += 1
        continue
    print("str[%d] = %s" % (index, str[index]))
    index += 1
