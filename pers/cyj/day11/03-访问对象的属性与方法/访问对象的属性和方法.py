class Person(object):
    """Person类"""

    # 定义属性（定义变量）
    name = "Sunny"
    age = 18
    height = 170
    weight = 70

    def run(self):
        print("run")

    def eat(self, food):
        print("eat:", food)

    def openDoor(self):
        print("我已经打开了冰箱门")

    def fillEle(self):
        print("我已经把大象装进冰箱了")

    def closeDoor(self):
        print("我已经关上了冰箱门")


if __name__ == "__main__":
    # 实例化对象
    per1 = Person()
    per2 = Person()

    """
    访问属性
    格式：对象名.属性名
    赋值：对象名.属性名 = 新值
    """
    print("姓名：%s, 年龄：%d, 身高：%d, 体重：%d, " % (per1.name, per1.age, per1.height, per1.weight))
    print("姓名：%s, 年龄：%d, 身高：%d, 体重：%d, " % (per2.name, per2.age, per2.height, per2.weight))
    print("==================================================")

    per2.name = "Tom"
    per2.age = 20
    per2.height = 160
    per2.weight = 60
    print("姓名：%s, 年龄：%d, 身高：%d, 体重：%d, " % (per1.name, per1.age, per1.height, per1.weight))
    print("姓名：%s, 年龄：%d, 身高：%d, 体重：%d, " % (per2.name, per2.age, per2.height, per2.weight))
    print("==================================================")

    """
    访问方法
    格式：对象名.方法名(参数列表)
    """
    per1.openDoor()
    per1.fillEle()
    per1.closeDoor()
    print("==================================================")

    per1.eat("香蕉")
    print("==================================================")

    # 问题：目前来看Person创建的所有对象属性都是一样的
