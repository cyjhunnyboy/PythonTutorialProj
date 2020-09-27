"""
数字类型转换
注意：字符串转换其他类型（整数、浮点数），如果有其他字符会报错，只有作为正负号才有意义

"""
# 浮点数转换为整数
print(int(1.1))
print(int(1.9))
# 整数转换为浮点数
print(float(1))
print(float(300))
# 字符串转换为整数
print(int("123"))
# 字符串转换为浮点数
print(float("12.3"))

# ValueError: invalid literal for int() with base 10: 'abc'
# print(int("abc"))
# invalid literal for int() with base 10: '123abc'
# print(int("123abc"))
print(int("+123"))
# ValueError: invalid literal for int() with base 10: '12+3'
# print(int("12+3"))
print(int("-123"))
