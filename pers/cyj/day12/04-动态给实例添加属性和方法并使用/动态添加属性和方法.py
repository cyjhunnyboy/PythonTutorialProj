from types import MethodType


# 创建一个空类
class Person(object):
    # 限制动态添加的属性（只能添加小括号中的这些属性）
    __slots__ = ("name", "age", "say")
    pass


def say(self):
    print("My name is " + per.name)


if __name__ == "__main__":
    per = Person()

    # 动态添加属性，这体现了动态语言的特点（灵活）
    per.name = "Tom"
    print(per.name)

    """
    # 动态添加方法
    def say(self):
        print("My name is " + self.name)

    per.say =say
    # TypeError: say() missing 1 required positional argument: 'self'
    # 缺少参数“self"报错
    # per.say()
    # 打印“My name is Tom”
    per.say(per)
    """
    per.say = MethodType(say, per)
    per.say()

    # 思考：如果我们想要限制实例的属性怎么办？
    # 比如：只允许给对象添加name, age, height, weight属性
    # 解决：定义类的时候，定义一个特殊的属性（__slots__)，可以限制动态添加的属性
    # __slots__ = ("name", "age", "say")，规定了只有这些属性
    # per对象添加height报错
    # AttributeError: 'Person' object has no attribute 'height'
    # per.height = 170
    # print(per.height)
