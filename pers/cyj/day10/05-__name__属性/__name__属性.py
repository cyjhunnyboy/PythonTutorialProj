from pers.cyj.day10.mudule import my_module

"""
05-__name__属性：
    模块就是一个可执行的.py文件，一个模块被另一个程序引入。我们不想让模块中的某些代码执行，可以用
    __name__属性来使程序仅调用模块中的一部分

"""

my_module.sayGood()
