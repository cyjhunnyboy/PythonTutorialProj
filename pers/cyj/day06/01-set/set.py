"""
set: 类似dict，是一组key的集合，不存储value
本质：无序和无重复元素的集合
"""

# 创建
# 创建set需要一个list或者tuple或者dict作为输入集合
set1 = set([1, 2, 3, 4, 5])
print(set1)
# 重复元素在set中会自动被过滤
print(set([1, 2, 3, 3, 3, 4, 5]))
print(set([1, 2, 3, 3, 2, 1]))

set2 = set({1:"good", 2:"nice"})
print(set2)

# 添加
set3 = set([1, 2, 3, 4, 5])
set3.add(6)
print(set3)

# 可以添加重复的，但是不会有效果
set3.add(3)
print(set3)

# set的元素不能是列表，因为列表是可变的
# TypeError: unhashable type: 'list'
# set3.add([7, 8, 9])
# print(set3)

set3.add((7, 8, 9))
print(set3)

# set的元素不能是字典，因为字典是可变的
# TypeError: unhashable type: 'dict'
# set3.add({1:"a"})
# print(set3)

# 插入整个list、tuple、字符串，打碎插入
set4 = set([1, 2, 3, 4, 5])
set4.update([6, 7, 8])
print(set4)
set4.update((9, 10))
print(set4)
set4.update("sunny")
print(set4)

# 删除
set5 = set([1, 2, 3, 4, 5])
set5.remove(3)
print(set5)

# 遍历
set6 = set("sunny")
for i in set6:
    print(i)
# set没有索引的
# TypeError: 'set' object is not subscriptable
# print(set6[3])
for index, data in enumerate(set6):
    print(index, data)


set7 = set([1, 2, 3])
set8 = set([2, 3, 4])
# 交集 后生成一个新的集合
a1 = set7 & set8
print(a1)
print(type(a1))

# 并集
a2 = set7 | set8
print(a2)
print(type(a2))
