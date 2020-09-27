import os


path = os.path.abspath(".") + "\dir"


def getAllDirDeep(path):
    """栈模拟递归遍历目录"""

    stact = []
    stact.append(path)

    # 处理栈，当栈为空的时候结束循环
    while len(stact) != 0:
        # 从栈里取出数据
        dirPath = stact.pop()
        # print(dirPath)
        # 目录下所有文件
        fileList = os.listdir(dirPath)
        # print(fileList)

        # 处理每一个文件，如果是普通文件打印出来，如果是目录则将该目录的地址压栈
        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                # 是目录就压栈
                print("目录：" + fileName)
                stact.append(fileAbsPath)
            else:
                # 打印普通文件
                print("普通文件：" + fileName)


getAllDirDeep(path)
