"""
概念：是一个闭包，把一个函数当做参数返回一个替代版的函数，本质上就是一个返回函数的函数

"""

# 简单的装饰器
def func():
    print("Sunny is a good man")


# 需求：func1函数打印之前或之后打印一串*号，但不能修改func1函数
"""
def outer():
    print("*********************")
    func1()
    print("*********************")

outer()
"""

def outer(func):
    def inner():
        print("*********************")
        func()
    return inner

# f是函数func1的加强版本
f = outer(func)
f()
