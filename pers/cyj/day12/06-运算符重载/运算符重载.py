# 不同的数据类型加法会有不同的解释
print(1 + 2)
print("1" + "2")


class Calculator(object):

    def __init__(self, num):
        self.num = num

    # 运算符重载
    def __add__(self, other):
        return Calculator(self.num + other.num)

    # 方法重写
    def __str__(self):
        return "num = " + str(self.num)


if __name__ == "__main__":
    calc1 = Calculator(1)
    calc2 = Calculator(2)
    # TypeError: unsupported operand type(s) for +: 'Calculator' and 'Calculator'
    print(calc1 + calc2)
    # 等价于
    # print(calc1.__add__(calc2))
    print(calc1)
    print(calc2)
