import os

"""
os: 包含了普遍的操作系统的功能

"""

# 获取操作系统类型：nt->windows posix->Linux\Unix或者Mac OS X
print("操作系统类型：%s" % os.name)

# 打印操作系统详细的信息（Windows不支持
#print(os.uname())

# 获取操作系统中的所有环境变量
print(os.environ)

# 获取指定环境变量
print(os.environ.get("MYSQL_HOME"))

# 获取当前目录 ./dir/...
# .
print(os.curdir)

# 获取当前工作目录，即当前python脚本所在的目录
# E:\Code\Python\经典Python教程入门到精通\PythonTutorialProj\pers\cyj\day08\02-os模块
print(os.getcwd())

# 以列表的形式返回指定目录下的所有的文件
# ['os模块.py', 'temps.txt', '__init__.py']
print(os.listdir(os.getcwd()))

# 在当前目录下创建新目录
os.mkdir("Sunny")
# 删除当前目录下创建的目录
os.rmdir("Sunny")

# 获取文件属性
print(os.stat("temps.txt"))
# 重命名
os.rename("temps.txt", "temps.txt")

# 删除普通文件
#os.remove("file.txt")

# 运行shell命令
os.system("notepad") # 记事本
os.system("write") # 写字板
os.system("mspaint") # 画板
#os.system("msconfig") # 系统设置
# os.system("shutdown -s -t 500")
# os.system("shutdown -a")
# os.system("taskkill /f /im notepad.exe")

# 有些方法存在os模块里，还有些存在于os.path
# 查看当前的绝对路径
# E:\Code\Python\经典Python教程入门到精通\PythonTutorialProj\pers\cyj\day08\02-os模块\temps.txt
print(os.path.abspath("./temps.txt"))

# 拼路径
# 注意：参数2里开始不要有斜杠
p1 = r"E:\Code\Python\经典Python教程入门到精通\PythonTutorialProj\pers\cyj\day08\02-os模块"
p2 = r"temps.txt"
# E:\Code\Python\经典Python教程入门到精通\PythonTutorialProj\pers\cyj\day08\02-os模块\temps.txt
print(os.path.join(p1, p2))
# E:\Code\Python\经典Python教程入门到精通\PythonTutorialProj\pers\cyj\day08\02-os模块\temps.txt
print(os.path.join(os.path.abspath("."), "temps.txt"))

# 拆分路径
p3 = r"E:\Python\经典Python教程入门到精通\PythonTutorialProj\pers\cyj\day08\02-os模块\temps.txt"
# ('E:\\Python\\经典Python教程入门到精通\\PythonTutorialProj\\pers\cyj\\day08\02-os模块', 'temps.txt')
print(os.path.split(p3))
# 获取扩展名
# ('E:\\Python\\经典Python教程入门到精通\\PythonTutorialProj\\pers\cyj\\day08\02-os模块\\temps', '.txt')
print(os.path.splitext(p3))

# 判断是否是目录
p4 = r"E:\Python\经典Python教程入门到精通\PythonTutorialProj\pers\cyj\day08\02-os模块"
print(os.path.isdir(p3))
print(os.path.isdir(p4))

# 判断文件是否存在
print("判断文件是否存在：", os.path.isfile(p3))
print("判断文件是否存在：", os.path.isfile(p4))

# 判断目录是否存在
print("判断目录是否存在：", os.path.exists(p3))
print("判断目录是否存在：", os.path.exists(p4))

# 获得文件大小(字节）
print(os.path.getsize(p3))

# 文件的目录名
print(os.path.dirname(p3))
# 文件名
print(os.path.basename(p3))
