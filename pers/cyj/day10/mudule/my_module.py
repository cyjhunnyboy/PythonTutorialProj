# 一个.py文件就是一个模块

# 每一个模块都有一个__name__属性，当其值等于"__main__"时，表明该模块自身在执行。
# 否则引入了其他文件

# 当前文件如果为程序入口文件，则__name__属性为__main__
if __name__ == "__main__":
    print("这是my_module.py")
else:

    print(__name__)

    TT = 200


    def sayGood():
        print("Sunny is a good man!")


    def sayNice():
        print("Sunny is a nice man!")


    def sayHandsome():
        print("Sunny is a handsome man!")
