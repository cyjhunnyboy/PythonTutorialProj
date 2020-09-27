listNum = []
num = 0
while num < 10:
    val = int(input("请您输入一个数字："))
    listNum.append(val)
    num += 1
print(listNum)

# 升序排序
listNum.sort()

count = listNum.count(listNum[len(listNum) - 1])
c = 0
while c < count:
    listNum.pop()
    c += 1
print(listNum[len(listNum) - 1])
