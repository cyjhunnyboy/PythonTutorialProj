"""
for语句
    格式：
        for 变量名 in 集合：
            语句
    逻辑：按顺序取“集合”中的每个元素赋值给“变量”，再去执行语句。如此循环往复，直到取完“集合”中的元素截止

"""

for i in [1, 2, 3, 4, 5]:
    print(i)

"""
    range()函数，列表生成器，功能：生成序列
"""
print("=====================")
a = range(10)
print(a)
for x in range(10):
    print(x)

"""
range([start,] end[,step])函数
start：默认为0
step：默认为1
"""
print("=====================")
for y in range(2, 100, 2):
    print(y)

# 同时遍历下标和元素
print("=====================")
for index, m in enumerate([1, 2, 3, 4, 5]): # index, m = 下标，元素
    print(index, m)

# 1+2+3+4+.....+100
print("=====================")
sum = 0
for n in range(1, 101):
    sum += n
print(sum)
