from pers.cyj.day11.single.person import Person


class Student(Person):
    """学生类"""

    def __init__(self, name, age, money, stuId):
        # 调用父类中的__init__()
        super(Student, self).__init__(name, age, money)
        # 子类可以有一些自己独有的属性
        self.stuId = stuId

    def payTuitionFee(self):
        # 继承父类的私有属性，子类不能直接访问
        print("交学费：%d", self._money)
