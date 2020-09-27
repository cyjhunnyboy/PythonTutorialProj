"""
from.....import * 语句
作用：把一个模块中所有的内容全部导入当前命名空间

"""
# 最好不要过多的使用
from pers.cyj.day10.mudule.my_module import *

TT = 300

def sayGood():
    print("**************")

sayGood()
sayNice()
sayHandsome()
print(TT)
