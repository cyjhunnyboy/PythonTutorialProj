class Person(object):

    def __init__(self, age):
        # 属性直接对外暴露
        # self.age = age
        # 限制访问
        self.__age = age

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age < 0:
            age = 0
        self.__age = age


if __name__ == "__main__":

    per = Person(18)
    # 属性直接对外暴露
    # 不安全，没有数据的过滤
    # per.age = -10
    # print(per.age)

    # 使用限制访问，需要自己写set和get方法才能访问
    per.setAge(19)
    print(per.getAge())
