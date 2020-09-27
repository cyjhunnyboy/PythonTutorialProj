listNum = []
num = 0
while num < 5:
    val = int(input("请您输入一个数字："))
    listNum.append(val)
    num += 1
print(listNum)

if listNum[0] >= listNum[1]:
    max = listNum[0]
    sec = listNum[1]
else:
    max = listNum[1]
    sec = listNum[0]

index = 2
while index < len(listNum):
    if listNum[index] >= sec:
        sec = listNum[index]
    if listNum[index] >= max:
        sec = max
        max = listNum[index]
    index += 1
print(sec)
