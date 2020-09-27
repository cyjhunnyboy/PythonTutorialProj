# 存储5个人的年龄，求他们的平均年龄
age1 = 18
age2 = 19
age3 = 20
age4 = 21
age5 = 22
print("平均年龄是：%d" % ((age1 + age2 + age3 + age4 + age5) / 5))

# 思考：要存储100个人的年龄
# 解决：使用列表
# 本质：是一种有序的集合

"""
创建列表
    格式：列表名 = [列表选项1,列表选项2,...,列表选项n]
"""
# 创建一个空列表
list1 = []
print(list1)
# 创建一个带有元素的列表
list2 = [18, 19, 20, 21, 22]
index = 0
sum = 0
# 嵌套最好不要超过3层
while index < 5:
    sum += list2[index]
    index += 1
    if index == 5:
        print("平均年龄：%d" % (sum / 5))

# 注意：列表中的元素数据可以是不同类型的
list3 = [1, 2, "Sunny", "Good", True]
print(list3)

# 列表元素的访问
# 取值 格式：列表名[下标] 下标也是从零开始
list4 = [1, 2, 3, 4, 5]
print(list4[2])

# 替换
list4[2] = 300
print(list4)
# 注意：不要越界（下标超出了可表示的范围）
# IndexError: list assignment index out of range
# list4[5] = 200
# print(list4)
