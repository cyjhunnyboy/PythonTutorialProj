# 从控制台输入一个数，分解质因数
# 90=2*3*3*5
num = int(input("请输入一个数："))
i = 2
while num != 1:
    if num % i == 0:
        print(i)
        num //= i
    else:
        i += 1
