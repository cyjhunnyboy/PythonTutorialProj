class Animal(object):
    """动物类"""

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + "吃！")
