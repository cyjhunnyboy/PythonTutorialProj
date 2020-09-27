"""
值传递：传递的是不可变类型
不可变类型：string，tuple，number


引用传递：传递的是可变类型
可变类型：list，dict，set

"""

def func1(num):
    print("函数中temp的地址是：%s" % id(num))
    print("函数中temp = %d" % num)
    num = 10
    print("函数中num的地址是：%s" % id(num))
    print("函数中num = %d" % num)


temp = 20
# num = temp
func1(temp)
print("temp的地址是：%s" % id(temp))
print("temp = %d " % temp)
print("==============================")


def func2(list1):
    list1[0] = 100
    print("函数中list1的地址是：%s" % id(list1))
    print("函数中list1 = %s" % list1)


list2 = [1, 2, 3, 4, 5]
func2(list2)
print("list2的地址是：%s" % id(list2))
print("list2 = %s" % list2)


print("==============================")
a = 10
b = 10
print(id(a), id(b))
c = 20
d = 30
print(id(c), id(d))
d = c
print(id(c), id(d))

