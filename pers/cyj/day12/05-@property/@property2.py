"""
property: 可以让你对受限制访问的属性使用点语法

"""

class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # 方法名为受限制的变量去掉双下划线
    @property
    def age(self):
        return self.__age

    # 去掉双下划线.setter
    @age.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age


if __name__ == "__main__":
    per = Person("Tom", 18)
    # 相当于调用setAge
    per.age = 100
    # 相当于调用getAge
    print(per.name, per.age)
