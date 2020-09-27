"""
需求：当程序遇到问题时不让程序结束，而越过错误继续向下执行

try.....except.....finally
格式：
    try:
        语句t
    except 错误码 as e:
        语句1
    except 错误码 as e:
        语句2
    .....
    except 错误码 as e:
        语句n
    finally:
        语句f

作用: 语句t无论是否有错误都将执行最后的语句f
"""

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("除数为零了")
finally:
    print("必须执行我！")
print("***************")
