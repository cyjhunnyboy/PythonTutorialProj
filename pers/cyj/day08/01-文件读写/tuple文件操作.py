# 数据持久性模块
import pickle
import os

tuple = (1, 2, 3, 4, 5, "Sunny is a good man凯")


path = os.path.abspath(".") + "\\files\\tuple.txt"


with open(path, "wb") as fWrite:
    pickle.dump(tuple, fWrite)


with open(path, "rb") as fRead:
    tempTuple = pickle.load(fRead)
    print(tempTuple)
