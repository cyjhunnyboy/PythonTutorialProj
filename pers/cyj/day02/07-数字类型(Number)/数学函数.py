# 导入库
# 库：封装一些功能
# math：数学相关的库
import math
import random


# 返回数字的绝对值
a1 = -10
a2 = abs(a1)
print(a2)
print(id(a1))
print(id(a2))

print((6 > 9) - (6 < 9))
print((10 > 9) - (10 < 9))
print((9 > 9) - (9 < 9))

# 比较两个数的大小
a3 = 6
a4 = 9
print((a3 > a4) - (a3 < a4))
# 返回给定参数的最大值
print("a3与a4比较，最大值是：", max(a3, a4))
# 返回给定参数的最小值
print("a3与a4比较，最小值是：", min(a3, a4))
# 求x的y次方 比如2的5次方
print("2的5次方等于：", pow(2, 5))
# round(x[,n])返回浮点数x的四舍五入的值，如果给出n值，则代表舍入到小数点后n位
print(round(3.456))
print(round(3.456, 1))
print(round(3.456, 2))

# 向上取整ceil
print(math.ceil(18.1))
print(math.ceil(18.9))

# 向下取整
print(math.floor(18.1))
print(math.floor(18.9))

# 返回整数部分与小数部分，都是浮点数
# (0.3000000000000007, 22.0)
print(math.modf(22.3))

# 开方，结果是浮点数
print(math.sqrt(16))

# 随机数
# 从序列的元素中随机挑选一个元素
print(random.choice([1, 3, 5, 7, 9]))
print(random.choice([1, 3, "abc"]))
# range(5) = [0, 1, 2, 3, 4]
print(random.choice(range(5)))
# "sunny" = ["s", "u", "n", "n", "y"]
print(random.choice("sunny"))

# 生成一个1~100之间的随机数
r1 = random.choice(range(10)) + 1
print("r1 = ", r1)

# random.randrange([start,] stop[, step])
# 从指定范围内，按指定的基数递增的集合中选取一个随机数
# start--指定范围的开始值，包含在范围内，默认是0
# stop--指定范围的结束值，不含在范围内
# step--指定的递增基数，默认是1
print(random.randrange(1, 100, 2))
# 从0~99选取一个随机数
print(random.randrange(100))

# 随机生成一个[0, 1)之间的数（浮点数）
print(random.random())

list = [1, 2, 3, 4, 5]
# 将序列的所有元素随机排序
random.shuffle(list)
print(list)

# 随机生成一个实数，在[3, 9]范围内
print(random.uniform(3, 9))
