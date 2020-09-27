# len() 返回元组中元素的个数
t01 = (1, 2, 3, 4, 5)
print(len(t01))

# max() 返回元组中的最大值
print(max((5, 6, 7, 8, 9)))

# min() 返回元组中的最小值
print(min((5, 6, 7, 8, 9)))

# 将列表转为元组
list = [1, 2, 3]
t02 = tuple(list)
print(t02)

# 元组的遍历
print("===========================")
for i in (1, 2, 3, 4, 5):
    print(i)
