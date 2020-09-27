"""
概念：能处理比定义时更多的参数

"""
# 加了星号（*）的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元组
def func(name, *args):
    str = name
    print(type(args))
    for x in args:
        str += x
    print(str)


func("Sunny", " is a good", " man")


# 求多个数和的函数
def my_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(my_sum(1, 2, 3, 4, 5))


# **代表键值对的参数字典，和*所代表的意义类似
# *代表的是元组
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))

func2(x = 1, y = 2, z = 3)
# TypeError: func2() takes 0 positional arguments but 3 were given
# func2(1, 2, 3)


# 表示可以传任意参数
def func3(*args, **kwargs):
    pass # 代表一个空语句