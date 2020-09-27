"""
需求：编写一个函数，给函数一个姓名和一个年龄，在函数内部打印出来

"""
# 形参（形式参数）：定义函数时小括号中的变量叫做形式参数，本质是变量
def my_print1(name, age):
    print("姓名 = %s，年龄 = %d" % (name, age))



# 调用函数
# 实参（实际参数）：调用函数时给函数传递的数据，本质是值
# 函数调用的本质其实就是实参给形参赋值的过程
# 参数必须按顺序传递，个数目前要对应
my_print1("Tom", 16)
my_print1("John", 16)
my_print1("Smith", 16)
name1 = "张三"
age1 = 19
my_print1(name1, age1)


def my_print2(name, age, hoby):
    print("姓名 = %s，年龄 = %d" % (name, age))


# 参数必须按顺序传递，个数目前要对应
# TypeError: my_print2() missing 1 required positional argument: 'hoby'
# my_print2("Tom", 22)
my_print2("李四", 25, None)
