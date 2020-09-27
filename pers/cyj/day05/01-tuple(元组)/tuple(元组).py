"""
tuple 元组
本质：是一种有序的集合
特点：
1、与列表非常相似
2、一旦初始化不能修改
3、使用小括号
"""
# 创建元组
# 格式：元组名 = (元组元素1, 元组元素2, ......, 元组元素n)


# 创建空的元组
tuple1 = ()
print(tuple1)
# 创建带有元素的元组
# 元组中的元素的类型可以不同
tuple2 = (1, 2, 3, "good", True)
print(tuple2)
# 定义只有一个元素的元组
tuple3 = (1,)
print(tuple3)
print(type(tuple3))

# 元组元素的访问
# 格式：元组名[下标]
tuple4 = (1, 2, 3, 4, 5)
print(tuple4[0])
print(tuple4[1])
print(tuple4[2])
print(tuple4[3])
print(tuple4[4])
# IndexError: tuple index out of range
# print(tuple4[5]) # 下标超过范围（越界）

# 获取最后一个元素
print(tuple4[-1])
# 获取倒数第二个元素
print(tuple4[-2])
print(tuple4[-3])
print(tuple4[-4])
print(tuple4[-5])
# IndexError: tuple index out of range
# print(tuple4[-6]) # 下标超过范围（越界）


# 修改元组
tuple5 = (1, 2, 3, 4, 5)
# TypeError: 'tuple' object does not support item assignment
# 元组一旦初始化，就不能进行修改
# tuple5[0] = 100
print(tuple5)

tuple6 = (1, 2, 3, 4, [5, 6, 7])
tuple6[-1][0] = 500
print(tuple6)

# 删除元组
tuple7 = (1, 2, 3)
del tuple7
# NameError: name 'tuple7' is not defined
# print(tuple7)


# 元组的操作
tuple8 = (1, 2, 3)
tuple9 = (4, 5, 6)
tuple10 = tuple8 + tuple9
print(tuple10)
print(tuple8)
print(tuple9)

# 元组重复
tuple11 = (1, 2, 3)
print(tuple11 * 3)

# 判断元素是否在元组中
tuple12 = (1, 2, 3)
print(1 in tuple12)
print(4 in tuple12)

# 元组的截取
# 格式：元组名[开始下标:结束下标]
# 从开始下标开始截取，截取到结束下标之前
tuple13 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple13[3:7])
print(tuple13[:7])
print(tuple13[7:])
print(tuple13[:])
print(tuple13)


# 二维元组: 元素为一维元组的元组
tuple14 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tuple14[1][1])
