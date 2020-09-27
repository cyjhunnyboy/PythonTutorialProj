"""
Python全部的错误类型:
 
ZeroDivisionError	除(或取模)零 (所有数据类型)
ValueError	传入无效的参数
AssertionError	断言语句失败
StopIteration	迭代器没有更多的值
IndexError	序列中没有此索引(index)
IndentationError	缩进错误
OSError	输入/输出操作失败
ImportError	导入模块/对象失败
NameError	未声明/初始化对象 (没有属性)
AttributeError	对象没有这个属性
 	 
GeneratorExit	生成器(generator)发生异常来通知退出
TypeError	对类型无效的操作
KeyboardInterrupt	用户中断执行(通常是输入^C)
OverflowError	数值运算超出最大限制
FloatingPointError	浮点计算错误
BaseException	所有异常的基类
SystemExit	解释器请求退出
Exception	常规错误的基类
StandardError	所有的内建标准异常的基类
ArithmeticError	所有数值计算错误的基类
EOFError	没有内建输入,到达EOF 标记
EnvironmentError	操作系统错误的基类
WindowsError	系统调用失败
LookupError	无效数据查询的基类
KeyError	映射中没有这个键
MemoryError	内存溢出错误(对于Python 解释器不是致命的)
UnboundLocalError	访问未初始化的本地变量
ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	一般的运行时错误
NotImplementedError	尚未实现的方法
SyntaxError Python	语法错误
TabError	Tab 和空格混用
SystemError	一般的解释器系统错误
UnicodeError	Unicode 相关的错误
UnicodeDecodeError	Unicode 解码时的错误
UnicodeEncodeError	Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
以下为警告类型	 
Warning	警告的基类
DeprecationWarning	关于被弃用的特征的警告
FutureWarning	关于构造将来语义会有改变的警告
OverflowWarning	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	可疑的语法的警告
UserWarning	用户代码生成的警告
"""