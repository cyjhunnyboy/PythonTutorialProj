"""
成员运算符：
in: 如果在指定的序列中找到值返回True, 否则返回False
not in: 如果在指定的序列中没有找到值返回True, 否则返回False
"""
list = [1, 2, 3, 4, 5]
a = 3
b = 6
if a in list:
    print("a是list的元素")
else:
    print("a不是list的元素")

if b not in list:
    print("b不是list的元素")
else:
    print("b是list的元素")
