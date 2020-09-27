import os

path = os.path.abspath(".") + "\dir"


def getAllDir(path, space = ""):

    # 得到当前目录下所有的文件
    fileList = os.listdir(path)
    # 处理每一个文件
    space += "---"
    for fileName in fileList:
        # path\fileName
        # 判断是否是路径(绝对路径)
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(space + "目录：", fileName)
            getAllDir(fileAbsPath, space)
        else:
            print(space + "普通文件：", fileName)


getAllDir(path)
