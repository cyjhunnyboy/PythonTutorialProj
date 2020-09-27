def a():
    print("****************")

# 普通函数调用
def func():
    a()

"""
递归调用：一个函数，调用了自身，称为递归调用
递归函数：一个会调用自身的函数称为递归函数

凡是循环能干的事，递归都能干

方式：
1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再次求出本次的结果
"""

# 输入一个数(大于等于1)，求1+2+3+......+n的和
def sum1(n):
    sum = 0
    for x in range(1, n + 1):
        sum += x
    return sum


result = sum1(100)
print("result = ", result)
print("=======================")

"""
1+2+3+4+5
sum2(1) + 0 = sum2(1)
sum2(1) + 2 = sum2(2)
sum2(2) + 3 = sum2(3)
sum2(3) + 4 = sum2(4)
sum2(4) + 5 = sum2(5)

5 + sum2(4)
5 + 4 + sum2(3)
5 + 4 + 3 + sum2(2)
5 + 4 + 3 + sum2(1)
5 + 4 + 3 + 2 + 1

5 * multiply(4)
5 * 4 * multiply(3)
5 * 4 * 3 * multiply(2)
5 * 4 * 3 * 2 * multiply(1)
5 * 4 * 3 * 2 * 1
"""
def sum2(n):
    if n == 1:
        return 1
    else:
        return n + sum2(n - 1)


result2 = sum2(100)
print("result2 = ", result2)


def multiply(n):
    if n == 1:
        return 1
    else:
        return n * multiply(n - 1)


result3 = multiply(5)
print("result3 = ", result3)