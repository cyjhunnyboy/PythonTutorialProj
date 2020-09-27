def sum(*args):
    """计算n个数的和"""
    sum = 0
    for i in args:
        sum += i
    return sum


def multiply(*args):
    """计算n个数相乘"""
    result = args[0]
    for i in args[1:]:
        result *= i
    return result


if __name__ == "__main__":

    print("1+2+..+10的和是：", sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print("1*2*..*10的结果是：", multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
