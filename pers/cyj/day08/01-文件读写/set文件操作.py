# 数据持久性模块
import pickle
import os

set = set({"张三": 60, "Tom": 80, "李四": 90})


path = os.path.abspath(".") + "\\files\set.txt"


with open(path, "wb") as fWrite:
    pickle.dump(set, fWrite)


with open(path, "rb") as fRead:
    tempSet = pickle.load(fRead)
    print(tempSet)
