"""
if语句嵌套if语句
"""
num1 = 10
num2 = 10
if num1 == num2:
    num1 = 20
    if 1:
        print("******")
        print("num1 = ", num1)
