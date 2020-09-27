"""
概念：允许函数调用时参数的顺序与定义时不一致

"""
def my_print(str, age):
    print(str, age)


# 使用关键字参数
my_print(age = 18, str="Sunny is a good man")
