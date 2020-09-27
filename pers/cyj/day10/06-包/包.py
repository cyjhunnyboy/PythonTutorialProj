from pers.cyj.day10.mudule.calc import calculator as calc
from pers.cyj.day10.mudule.sum import calculator as sum

"""
思考：如果不同的人编写的模块同名怎么办？

解决：为了解决模块命名的冲突问题，引入了按目录来组织模块的方法，称为包

特点：引入了包以后，只要顶层的包不与其他人发生冲突，那么模块都不会与别人的发生冲突

注意：目录只有包含一个叫做"__init__.py"的文件才被认作是一个包，主要是为了避免一些滥竽充数的名字，但是基本上目前这个文件中什么也不用写

"""

print(calc.sum(1, 2, 3, 4, 5))
print(sum.sum(1, 2, 3, 4, 5))
