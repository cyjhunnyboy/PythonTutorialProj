class Mother(object):
    """母亲类"""

    def __init__(self, faceValue):
        self.faceValue = faceValue

    def play(self):
        print("Mother类：play")

    def eat(self, food):
        print("Mother类--eat: %s" % food)
