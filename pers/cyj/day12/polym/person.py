class Person(object):
    """定义一个人类"""

    def feedCat(self, cat):
        print("给你食物")
        cat.eat()

    def feedMouse(self, mouse):
        print("给你食物")
        mouse.eat()

    def feedAnimal(self, animal):
        print("给你食物")
        animal.eat()
