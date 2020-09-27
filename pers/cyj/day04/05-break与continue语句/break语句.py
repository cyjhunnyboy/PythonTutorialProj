"""
break语句：
作用：跳出for和while循环
注意：只能跳出距离它最近的那一层循环
"""

for i in range(10):
    print(i)
    if i == 5:
        # 结束整个循环
        break


print("==================")
num = 1
while num <= 10:
    print(num)
    if num == 6:
        break
    num += 1
# 注意：循环语句可以有else语句，break导致循环截止，不会执行else下面的语句
else:
    print("Sunny is a good man!")
