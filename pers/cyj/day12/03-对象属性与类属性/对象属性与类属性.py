class Person(object):
    # 这里的属性实际上属于类属性（用类名来调用）
    name = "person"

    # init函数作用给对象添加属性，并初始化
    def __init__(self, name):
        # 对象属性
        self.name = name
        # pass


if __name__ == "__main__":
    # 类属性
    print(Person.name)  # 打印“person"
    per = Person("Tom")

    # 对象属性
    # 对象属性的优先级高于类属性，若仅仅有类属性，没有同名的对象属性，则使用类属性
    # 若同时有同名的类属性和对象属性，则使用的是对象属性
    print(per.name)  # 打印“Tom”

    # 动态的给对象添加属性（属于该对象的属性）
    # 只针对于当前对象生效，对于类创建的其他对象没有作用
    per.age = 18
    print(per.age)

    per2 = Person("Sunny")
    # AttributeError: 'Person' object has no attribute 'age'
    # age属性是per对象的属性，不属于per2的对象属性，会报错
    # print(per2.age)

    # 删除对象中的name属性
    del per.name
    # 调用同名的类属性
    # 打印“person"
    print(per.name)

    # 注意：以后千万不要将对象属性与类属性重名，因为对象属性会屏蔽掉类属性
    # 但是当删除对象属性后，再使用又能使用类属性了

