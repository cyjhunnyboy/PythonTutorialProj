"""
概念：调用函数时，如果没有传递参数，则使用默认参数

"""

def my_print(str = "Sunny is a good man", age = 18):
    print(str, age)


my_print()
my_print("Tom is a handsome man", 19)


# 以后要使用默认参数，最好将默认参数放到最后
def my_print1(str, age = 19):
    print(str, age)


my_print1("Sunny is a good man")
