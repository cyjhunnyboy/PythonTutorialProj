# 装饰器
def outer(func):
    def inner(*args, **kwargs):
        # 添加修改的功能
        print("*****************")
        func(*args, **kwargs)
        print("*****************")
    return inner

@outer
def say(name, age):
    print("My name is %s, I'm %d years old!" % (name, age))


# 函数的参数理论上是无限制的，但是实际上最好不要超过6、7个
say("John", 18)
