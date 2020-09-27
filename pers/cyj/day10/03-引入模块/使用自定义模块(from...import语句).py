# from...import语句
# 作用：从模块中导入一个指定的部分到当前命名空间
# 格式：from module import name1[,name2[,...namen]]]
from pers.cyj.day10.mudule.my_module import sayNice

"""
程序中的函数可以将模块中的同名函数或变量覆盖
"""

TT = 300

def sayGood():
    print("*******")

sayGood()
sayNice()
print(TT)
# NameError: name 'sayHandsome' is not defined
# 没有引入sayHandsome函数，所以报错
# sayHandsome()
