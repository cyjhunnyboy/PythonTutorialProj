"""
引用模块
import语句
格式：import module1[,module2[,module3[,....modulen]]]

使用模块中的内容
格式：模块名.函数名/变量名
"""
# 引用了自定义模块，不用加.py后缀
import pers.cyj.day10.mudule.my_module as my_module
# 一个模块只会被引入一次，不管你执行了多少次import，防止模块被多次引入
# import pers.cyj.day10.my_module as my_module

TT = 300

def sayGood():
    print("*************")


my_module.sayGood()
my_module.sayNice()
my_module.sayHandsome()
print(my_module.TT)
