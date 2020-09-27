from pers.cyj.day11.single.person import Person


class Worker(Person):
    """工人类"""

    def __init__(self, name, age, money):
        super().__init__(name, age, money)
