"""
概述：使用键-值（key-value)存储，具有极快的查找速度

key的特性：
1、字典中的key必须唯一
2、key必须是不可变的对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变的，不能作为key

思考：保存多位学生的姓名与成绩？
[["Tom", "2020010001", 60], ["John", "2020010002",  70]]
使用列表，无法区分学生学号和成绩，使用字典，学生姓名为Key，学生成绩作为值

注意：字典是无序的
"""
# 字典的创建
dict1 = {"Tom": 60, "John": 80}


# 元素的访问
# 格式：字典名[key]
print("Tom的成绩是：%d" % dict1["Tom"])
# TypeError: 'type' object is not subscriptable
# print(dict["Sun"])
# 根据key查找没有返回：None，一般通过这种方式找
print(dict1.get("Sun"))
res = dict1.get("Sun")
if res is None:
    print("没有")
else:
    print("有")


# 添加
print("==============================")
dict1["Anny"] = 80
# 因为一个key对应一个value，因此，多次对一个key的value赋值
# 其实是修改值
dict1["Tom"] = 90
print(dict1)


# 删除
print("==============================")
dict1.pop("Anny")
print(dict1)


# 遍历dict1
print("==============================")
for key in dict1:
    print(key, dict1[key])


# 遍历value
print("==============================")
# 打印出来是列表
print(dict1.values())
for value in dict1.values():
    print(value)


# 遍历key，value
print("==============================")
# 打印出来是一个元组
print(dict1.items())
for key, value in dict1.items():
    print(key, value)


# 枚举方式遍历
print("==============================")
for i, v in enumerate(dict1):
    print(i, v)


"""
dict和list比较
1、查找和插入的速度极快，不会随着key-value的增加而变慢
2、需要占用大量的内存，内存浪费多

list的优缺点：
1、查找和插入的速度随着数据的增多而减慢
2、占用空间小，浪费内存小
"""
print("==============================")
w = "man"
str1 = "Sunny is a good man! Sunny is a nice man! Sunny is a handsome man! Sunny is a great man! Sunny is a noble man! Sunny is a cool man!"
print(str1.count(w))
