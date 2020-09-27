# 需求：打印之前输出一串*号，打印之后输出一串*号，且不能修改say函数
"""
装饰器格式：
def outer(func):
    def inner():
        pass
    return inner
"""
def outer(func):
    def inner(name, age):
        if age < 0:
            age = 0
        print("*********************")
        func(name, age)
        print("*********************")
    return inner


# 使用@符号将装饰器应用到函数
# 相当于：say = outer(say)
@outer
def say(name, age):
    print("%s is %d years old" % (name, age))


# say("Sunny", -19)
# say = outer(say)
say("Tom", -19)
