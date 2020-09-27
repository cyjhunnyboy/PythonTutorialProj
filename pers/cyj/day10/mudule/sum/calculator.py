def sumTwo(a, b):
    """计算两个数之和"""
    return a + b


def sumThree(a, b, c):
    """计算三个数之和"""
    return a + b + c


def sum(*args):
    """计算n个数相加"""
    sum = 0
    for i in args:
        sum += i
    return sum


if __name__ == "__main__":

    print(sumTwo(8, 9))
    print(sumThree(8, 9, 10))
    print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
