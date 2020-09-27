"""
变量
1、定义：程序可操作的存储空间的名称，或者程序运行期间能改变的数据，或者每个变量都有特定的类型
2、作用：将不同类型的数据存储到内存
3、定义变量：变量名=初始值（为了确定变量的类型）， 如： age = 0
4、数据的存储：变量名 = 数据值
5、注意：变量在使用之前必须定义，否则会报错
6、删除变量：del 变量名，删除后变量无法引用
7、程序执行的过程：自上而下顺序执行(面向过程)
8、查看变量的类型：type(变量名)
9、查看变量的地址：id(变量名）

"""

age = 0

print("age = ", age)

age = 18

print("age = ", age)

# 变量未定义，报错 NameError: name 'score' is not defined
# print("score = ", score)

num1 = int(input("请输入一个数字："))
num2 = int(input("请再输入一个数字："))

print("num1 + num2 = ", num1 + num2)

print("age 的类型是：", type(age))
print("age 的类型是：", id(age))

age = 19.5

print("age 的类型是：", type(age))
print("age 的类型是：", id(age))

age = "good"

print("age 的类型是：", type(age))
print("age 的类型是：", id(age))
