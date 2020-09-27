"""
析构函数：__del__()
功能：释放对象时自动调用
"""


class Person(object):
    """Person类"""

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __del__(self):
        print("这里是析构函数")

    def run(self):
        print("run")

    def eat(self, food):
        print("eat:", food)

    def say(self):
        print("Hello, My name is %s, I'm %d years old!" % (self.name, self.age))


# 在函数里定义的对象，会在函数结束时自动释放
# 这样可以用来减少内存空间的浪费
def func():
    per2 = Person("Tom", 18, 170, 60)
    per2.say()


if __name__ == "__main__":
    per = Person("Sunny", 19, 160, 60)
    per.say()
    # 手动释放对象
    del per
    # NameError: name 'per' is not defined
    # 对象释放以后就不能在访问了
    # print(per.say())

    func()
