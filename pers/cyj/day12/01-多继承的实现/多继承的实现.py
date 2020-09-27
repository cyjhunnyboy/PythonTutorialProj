from pers.cyj.day12.multipleinherit.children import Children


def main():
    child = Children(300, 100, "Sunny")
    child.setAge(18)
    child.setGrade(6)
    print(child.money, child.faceValue)
    # 子类重写了父类同名方法，实际调用重写的方法
    child.play()
    # 注意：父类中方法名相同，默认调用的是在括号中排前面的父类中的方法
    child.eat("香蕉你个巴拉")
    # 子类特有的方法
    child.study()


if __name__ == "__main__":
    main()
