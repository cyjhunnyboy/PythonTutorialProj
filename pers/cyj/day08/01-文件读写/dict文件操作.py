# 数据持久性模块
import pickle
import os

dict = {"张三": 60, "Tom": 80, "李四": 90}


path = os.path.abspath(".") + "\\files\dict.txt"


with open(path, "wb") as fWrite:
    pickle.dump(dict, fWrite)


with open(path, "rb") as fRead:
    tempDict = pickle.load(fRead)
    print(tempDict)
