import os
import collections

path = os.path.abspath(".") + "\dir"


def getAllDirDreadth(path):
    """队列模拟递归遍历目录"""

    queue = collections.deque()
    # 进队
    queue.append(path)

    while len(queue) != 0:
        # 出队数据
        dirPath = queue.popleft()
        # 找出所有的文件
        fileList = os.listdir(dirPath)

        for fileName in fileList:
            # 绝对路径
            fileAbsPath = os.path.join(dirPath, fileName)
            # 判断是否是目录，是目录就进队，不是就打印
            if os.path.isdir(fileAbsPath):
                print("目录：" + fileName)
                queue.append(fileAbsPath)
            else:
                print("普通文件：" + fileName)



getAllDirDreadth(path)
