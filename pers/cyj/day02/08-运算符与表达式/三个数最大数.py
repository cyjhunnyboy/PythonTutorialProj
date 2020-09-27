# 从控制台输入三个数，输出较大的值(不准使用max\min函数)
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
num3 = int(input("请输入第三个整数："))
max = num1
if num2 > num1:
    max = num2
if num3 > max:
    max = num3
print("最大的数是：", max)
