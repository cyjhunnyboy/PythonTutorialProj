"""
构造函数：__init__()
功能：在使用类创建对象的时候自动调用
注意：如果不显式地写出构造函数，默认会自动添加一个空的构造函数

"""


class Person(object):
    """Person类"""

    # 定义属性（定义变量）
    # name = "Sunny"
    # age = 18
    # height = 170
    # weight = 70

    # 构造函数
    def __init__(self, name, age, height, weight):
        # print(name, age, height, weight)
        # 定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        # print("这里是init")

    def run(self):
        print("run")

    def eat(self, food):
        print("eat:", food)


if __name__ == "__main__":
    # 实例化对象
    per = Person("Tome", 20, 160, 80)
    print(per.name, per.age, per.height, per.weight)
    print("==============================")

    per2 = Person("Sunny", 18, 175, 70)
    print(per2.name, per.age, per2.height, per2.weight)
