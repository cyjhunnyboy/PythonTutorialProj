"""
self: 代表类的实例，而非类

哪个对象调用方法，那么该方法中的self就代表那个对象

self.__class__ 代表类名

"""


class Person(object):
    """Person类"""

    def __init__(self, name, age, height, weight):
        print(self)
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def run(self):
        print("run")
        print(self.__class__)
        p = self.__class__("tt", 30, 10, 30)
        print("新对象：", p)

    def eat(self, food):
        print("eat:", food)

    def say(self):
        print(self)
        print("Hello, My name is %s, I'm %d years old!" % (self.name, self.age))

    # self不是关键字，换成其他的标识符也是可以的，但是帅的人都是用self
    def play(a):
        print("play " + a.name)


if __name__ == "__main__":
    # 实例化对象
    per1 = Person("Tome", 20, 160, 80)
    per1.say()
    per1.play()
    per1.run()
    print("=============================")

    per2 = Person("Sunny", 18, 175, 70)
    per2.say()
