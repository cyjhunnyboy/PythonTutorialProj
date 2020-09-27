"""
如果要让内部属性不被外部直接访问，在属性前加两个下划线（__)，在Python中如果在属性前加两个下划线，
那么这个属性就变成了private（私有）属性

私有属性不能在类外部通过"对象名.私有属性"进行访问，但可以在类内部进行访问"对象名.私有属性"

通过自定义的方法（setMoney\getMoney)实现对私有属性的赋值与取值

不能直接访问私有属性的原因是因为Python解释器把私有属性变成了另一个名字
如：__money 变成  _Person__money  即变成了：_类名__属性名
仍然可以用（_类名__属性名）去访问，但是强烈建议不要这么干（帅的人都不这么干）
不同版本的解释器可能存在解释的变量名不一致

注意：在Python中：__属性名__ 属于特殊变量，可以直接访问

在Python中：_属性名，这样的实例变量外部是可以访问的，但是，按照约定的规则：当我们看到这样的变量时，
意思是“虽然我可以被访问，但是请把我视为私有变量，不要直接访问我
"""


class Person(object):
    """Person类"""

    def __init__(self, name, age, height, weight, money):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money
        # self.__age1__ = 0
        # self._age2 = 1

    # 通过内部方法，去修改私有属性
    def setMoney(self, money):
        # 数据的过滤
        if money < 0:
            money = 0
        self.__money = money

    # 通过内部方法，获取私有属性值
    def getMoney(self):
        return self.__money

    def run(self):
        # 私有属性内部可以使用
        # print(self.__money)
        print("run")

    def eat(self, food):
        print("eat:", food)

    def say(self):
        print("Hello, My name is %s, I'm %d years old!" % (self.name, self.age))


if __name__ == "__main__":
    per = Person("John", 18, 170, 70, 8000)
    # AttributeError: 'Person' object has no attribute '__money'
    # 私有属性不能被外部访问
    # per.__money = 9000 # 动态添加私有属性，与类中定义的私有属性名一致
    # print(per.name, per.__money)

    # 对象动态添加属性并打印
    # per.__wife = "Sunny"
    # print(per.__wife)

    # per.run()

    per.setMoney(10000)

    print(per.getMoney())

    # 强烈不建议这样访问私有属性，因为不同版本解释器可能存在解释的变量名不一致
    # per._Person__money = 11000
    # print(per.getMoney())

    # 特殊属性可以直接访问
    # print(per.__age1__)

    # print(per._age2)
