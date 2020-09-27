class Father(object):
    """父亲类"""

    def __init__(self, money):
        self.money = money

    def play(self):
        print("Father类：play")

    def eat(self, food):
        print("Father类--eat: %s" % food)
