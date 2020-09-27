from pers.cyj.day12.polym.animal import Animal

class Cat(Animal):
    """定义猫类"""

    def __init__(self, name):
        # 方式一：
        # super(Cat, self).__init__(name)
        # 方式二：
        super().__init__(name)
