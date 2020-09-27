"""
重写：将函数重新定义写一遍

__str__(): 在调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法
__repr__(): 是给机器用的，在Python解释器里面直接敲对象名再回车后调用的方法

注意：在没有str时，且有repr, str=repr

优点：当一个对象的属性值很多，并且都需要打印，重写了__str__()方法后，简化了代码

"""


class Person(object):
    """Person类"""

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return "Person(name=%s,age=%d,height=%d,weight=%d)" % (self.name, self.age, self.height, self.weight)

    def __repr__(self):
        return "这里是__repr__"


if __name__ == "__main__":
    # 重写__str__之前打印对象：<__main__.Person object at 0x000002128ECC94C0>
    # 重写__str__之后打印对象：Person(name=Sunny,age=18,height=170,weight=70)
    per1 = Person("Sunny", 18, 170, 70)
    print(per1)
    print(per1.__str__())
