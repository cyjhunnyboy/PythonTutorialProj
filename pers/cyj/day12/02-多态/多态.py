from pers.cyj.day12.polym.cat import Cat
from pers.cyj.day12.polym.mouse import Mouse
from pers.cyj.day12.polym.person import Person

"""
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物

"""

if __name__ == "__main__":
    tom = Cat("tom")
    jerry = Mouse("jerry")

    tom.eat()
    jerry.eat()

    print("=================")

    # 思考：再添加100中动物，也都有name属性和eat方法
    # 定义了一个有name属性和eat方法的Animal类，让所有的动物类都继承自Animal

    # 定义一个人类，可以喂猫和老鼠吃东西
    per = Person()
    per.feedCat(tom)
    per.feedMouse(jerry)

    print("=================")

    # 思考：人要喂100种动物，难道要写100个feed方法吗?
    # tom和Jerry都继承自动物
    per.feedAnimal(tom)
    per.feedAnimal(jerry)
