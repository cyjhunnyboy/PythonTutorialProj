"""
概述：目前代码比较少，写在一个文件中还体现不出什么缺点，但是
随着代码量越来越多，代码越来越难以维护，为了解决难以维护的问题，我们把很多相似功能的函数分组，
分别放到不同的文件中去，这样每个文件所包含的内容相对较少，而且对于每一个文件的大致功能可用文件名体现。
很多编程语言都是这么来组织代码结构的，一个.py文件就是一个模块

优点：
1、提高代码的可维护性
2、提高了代码的复用度，当一个模块完毕，可以被多个地方引用
3、引用其他的模块（内置模块和三方模块和自定义模块）
4、避免函数名和变量名的冲突

"""