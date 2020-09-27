# 列表方法

# append 在列表中的末尾添加新的元素
list1 = [1, 2, 3, 4, 5]
list1.append(6)
print(list1)
list1.append([7, 8, 9])
print(list1)

# extend 在末尾一次性追加另一个列表中的多个值
list2 = [1, 2, 3, 4, 5]
list2.extend([6, 7, 8])
# TypeError: 'int' object is not iterable
# list2.extend(9)
print(list2)

# insert 在下标处添加一个元素，不覆盖原数据，原数据向后顺延
list3 = [1, 2, 3, 4, 5]
list3.insert(1, 100)
print(list3)
list3.insert(2, [6, 7, 8])
print(list3)

# pop(x=list[-1]) 移除列表中指定下标处的元素（默认移除最后一个元素），并返回删除的数据
# 表示列表的最后一个下标
list4 = [1, 2, 3, 4, 5]
list4.pop()
print(list4)
list4.pop(2)
print(list4)
list4.pop(-1)
print(list4)
print(list4.pop(1))

# remove 移除列表中的某个元素第一个匹配的结果
list5 = [1, 2, 7, 3, 6, 4, 9, 4, 5, 6, 4]
list5.remove(4)
print(list5)

# clear 清除列表中所有的数据
list6 = [1, 2, 3, 4, 5]
list6.clear()
print(list6)

# index 从列表中找出某个值的第一个匹配的索引值
list7 = [1, 2, 3, 4, 5, 3, 6, 3]
index7_1 = list7.index(3)
print(index7_1)
# 圈定查找元素的范围（开始查找的位置、查找的结束位置）
index7_2 = list7.index(3, 3, 7)
print(index7_2)

# 列表中元素的个数
list8 = [1, 2, 3, 4, 5]
print(len(list8))

# 获取列表中的最大值
list9 = [1, 2, 3, 4, 5]
print(max(list9))

# 获取列表中的最小值
list10 = [1, 2, 3, 4, 5]
print(min(list10))

# 查看元素在列表中出现的次数
list11 = [1, 2, 3, 4, 5, 1, 3, 2, 3, 5, 6, 3, 3, 9]
print(list11.count(3))
num11 = 0
all = list11.count(3)
while num11 < all:
    list11.remove(3)
    num11 += 1
print(list11)

# reverse 倒叙
list12 = [1, 2, 3, 4, 5]
list12.reverse()
print(list12)

# 排序 升序
list13 = [1, 4, 3, 7, 9, 2, 5, 6, 8]
list13.sort()
print(list13)

# 拷贝
# 浅拷贝
list14 = [1, 2, 3, 4, 5]
list15 = list14
list14[1] = 200
print(list14)
print(list15)
print(id(list14))
print(id(list15))

# 深拷贝（内存的拷贝）
list16 = [1, 2, 3, 4, 5]
list17 = list16.copy()
list17[1] = 300
print(list16)
print(list17)
print(id(list16))
print(id(list17))

# 将元组转成列表
list18 = list((1, 2, 3, 4, 5))
print(list18)
