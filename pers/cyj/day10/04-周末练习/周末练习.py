import os
import collections

def work(srcPath, realPath):
    with open(srcPath, "r", encoding="utf-8") as fRead:
        while True:
            # laphae11985@163.com----198587
            lineInfo = fRead.readline()

            if len(lineInfo) < 5:
                break

            # 邮箱的字符串
            # laphae11985@163.com
            mailStr = lineInfo.split("----")[0]
            # 邮箱类型的目录
            # E:/Code/Python/经典Python教程入门到精通/PythonTutorialProj/pers/cyj/day10/res/163
            mailTypeStr = mailStr.split("@")[1].split(".")[0]
            dirStr = os.path.join(realPath, mailTypeStr)
            if not os.path.exists(dirStr):
                # 存在，创建
                os.mkdir(dirStr)
            # 创建文件
            filePath = os.path.join(dirStr, mailTypeStr + ".txt")
            with open(filePath, "a") as fWrite:
                fWrite.write(mailStr+"\n")


def getAllDirQueue(srcPath, realPath):
    """队列模拟递归遍历目录"""

    queue = collections.deque()
    queue.append(srcPath)

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
                queue.append(fileAbsPath)
            else:
                # 处理普通文件
                work(fileAbsPath, realPath)


if __name__ == "__main__":
    srcPath = os.path.abspath(".") + "/file/newdir"
    realPath = os.path.abspath(".") + "/file/res"
    getAllDirQueue(srcPath, realPath)