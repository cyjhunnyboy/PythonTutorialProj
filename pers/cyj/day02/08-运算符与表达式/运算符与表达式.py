"""
表达式：由变量、常量和运算符组成的式子

算术运算符和算术表达式
算术运算符：加(+) 减(-) 乘(*) 除(/)  取模(%) 求幂(**)  取整(//)
算术运算表达式
1 + 1  2 * 3  a / 3
功能：进行相关符号的数学运算，不会改变变量的值
值：相关的数学运算结果
"""
num1 = 5
num2 = 3
print("num1 + num2 = ", num1 + num2)
print("num1 - num2 = ", num1 - num2)
print("num1 * num2 = ", num1 * num2)
print("num1 / num2 = ", num1 / num2)
print("num1 % num2 = ", num1 % num2)
# 5**3 pow(5,3)
print("num1 ** num2 = ", num1 ** num2)
print("num1 // num2 = ", num1 // num2)

"""
赋值运算符和赋值运算表达式
赋值运算符：=
赋值运算表达式
格式：变量 = 表达式
功能：计算了等号右侧“表达式”的值，并赋值给等号左侧的变量
值：赋值结束后变量的值
"""
a = b = 1 + 3
print("a = ", a)
print("b = ", b)

num3 = 10
num4 = num3 + 20
print("num3 = ", num3)
print("num4 = ", num4)

"""
复合运算符
+=   a += b       a = a + b
-=   a -= b       a = a - b
*=   a *= b       a = a * b
/=   a /= b       a = a / b
%=   a %= b       a = a % b
**=  a **= b      a = a ** b
//=  a //= b      a = a // b
"""

num5 = 5
num6 = 3
num5 += num6
print("num5 += num6", num5)
num5 -= num6
print("num5 -= num6", num5)
num5 *= num6
print("num5 *= num6", num5)
num5 /= num6
print("num5 /= num6", num5)
num5 %= num6
print("num5 5%= num6", num5)
num5 **= num6
print("num5 **= num6", num5)
num5 //= num6
print("num5 //= num6", num5)
