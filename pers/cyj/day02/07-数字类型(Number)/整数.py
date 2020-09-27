"""
分类：整数、浮点数、复数
整数：Python可以处理任意大小的整数，当然包括负整数，在程序中的表示和数学的写法一样

"""
num1 = 10
num2 = num1
print("num1 = ", num1)
print("num2 = ", num2)
print("id(num1) = ", id(num1))
print("id(num2) = ", id(num2))
num1 = 20
print("num1 = ", num1)
print("num2 = ", num2)
print("id(num1) = ", id(num1))
print("id(num2) = ", id(num2))

# 连续定义多个变量
num3 = num4 = num5 = 1
print("num3 = %d, num4 = %d, num5 = %d" % (num3, num4, num5))
print("id(num3) = %s, id(num4) = %s, id(num5) = %s" % (id(num3), id(num4), id(num5)))


# 交互式赋值定义变量
num6, num7 = 6, 7
print("num6 = ", num6)
print("num7 = ", num7)
print("id(num6) = ", id(num6))
print("id(num7) = ", id(num7))
