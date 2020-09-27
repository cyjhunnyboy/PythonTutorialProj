# 引入模块
import sys

# 使用终端运行命令：python 使用标准库中的模块.py Sunny 18 羽毛球
print(sys.argv)

# 获取命令行参数的列表
for i in sys.argv:
    print(i)

name = sys.argv[1]

age = sys.argv[2]
hoby = sys.argv[3]

print(name, age, hoby)

# 自动查找所需模块的路径列表
print(sys.path)

