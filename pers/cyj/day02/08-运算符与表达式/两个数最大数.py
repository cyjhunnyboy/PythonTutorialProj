# 从控制台输入两个数，输出较大的值(不准使用max\min函数)
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))
if num1 > num2:
    max = num1
    print("最大的数是：", max)
else:
    max = num2
    print("最大的数是：", max)
