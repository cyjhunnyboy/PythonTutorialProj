# 数据持久性模块
import pickle
import os

list = [1, 2, 3, 4, 5, "Sunny is a good man凯"]


path = os.path.abspath(".") + "\\files\list.txt"


with open(path, "wb") as fWrite:
    pickle.dump(list, fWrite)


with open(path, "rb") as fRead:
    tempList = pickle.load(fRead)
    print(tempList)
