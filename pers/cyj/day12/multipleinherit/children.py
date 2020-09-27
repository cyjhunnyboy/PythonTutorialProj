from pers.cyj.day12.multipleinherit.father import Father
from pers.cyj.day12.multipleinherit.mother import Mother

class Children(Father, Mother):
    """孩子类"""

    def __init__(self, money, faceValue, name):
        Father.__init__(self, money)
        Mother.__init__(self, faceValue)
        self.name = name
        self.__age = 0
        self.__grade = 0

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age <0 or age > 150:
            print("你输入的年龄不正确")
            self.__age = 18
        else:
            self.__age = age

    def getGrade(self):
        return self.__grade

    def setGrade(self, grade):
        if grade < 0 or grade > 15:
            print("你输入的年级不合法")
            self.__grade = 3
        else:
            self.__grade = grade

    def play(self):
        print("Children类：play")

    def study(self):
        print("My name is %s, I'm %d 岁, I study %d 年级" %(self.name, self.__age, self.__grade))
