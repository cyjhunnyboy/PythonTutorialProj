"""
if-else语句
格式：
if 表达式:
    语句1
else:
    语句2
逻辑：当程序执行到if-else语句时，首先计算“表达式”的值，如果“表达式”的值为真，则执行“语句1”。执行完“语句1”跳出整个if-else语句。
如果“表达式”的值为假，则执行“语句2”，执行完“语句2”跳出这个if-else语句，继续向下继续
"""

num1 = 10
num2 = 20
if num1 == num2:
    num1 = 20
    print("num1 = ", num1)
else:
    num1 = 15
    print("num1 = ", num1)
