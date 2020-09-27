from pers.cyj.day11.single.student import Student
from pers.cyj.day11.single.worker import Worker


if __name__ == "__main__":
    stu = Student("Tom", 18, 800, 101001)
    print(stu.name, stu.age)
    stu.run()
    stu.eat("香蕉你个巴拉")
    print(stu.stuId)
    # AttributeError: 'Student' object has no attribute '_money'
    # stu.payTuitionFee()
    # AttributeError: 'Student' object has no attribute '__money'
    # 私有属性，不能在外部访问
    # print(stu.__money)
    # 通过继承过来的公共方法访问私有属性
    print(stu.getMoney())
    print("==================")

    work = Worker("Sunny", 20, 800)
    print(work.name, work.age)
    work.run()
    work.eat("吃你妹")
