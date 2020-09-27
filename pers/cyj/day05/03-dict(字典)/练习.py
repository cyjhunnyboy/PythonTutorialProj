"""
"Sunny is a good man! Sunny is a nice man! Sunny is a handsome man! Sunny is a great man! Sunny is a noble man! Sunny is a cool man!"
从控制台输入一串字符串，统计每个单词出现的次数

1、以空格切割字符串
2、循环处理列表中的每个元素
3、以元素当做key去一个字典中提取数据
4、如果没有提取到，就以该元素作为key，1作为value存进字典
5、如果提取到，将对应的key的value修改，值加1
6、根据输入的字符串当做key再去字典中取值
"""
w = input("请你输入要统计的单词：")
d = {}
str = "Sunny is a good man! Sunny is a nice man! Sunny is a handsome man! Sunny is a great man! Sunny is a noble man! Sunny is a cool man!"
l = str.split(" ")
for v in l:
    c = d.get(v)
    if c is None:
        d[v] = 1
    else:
        d[v] += 1

print(d[w])