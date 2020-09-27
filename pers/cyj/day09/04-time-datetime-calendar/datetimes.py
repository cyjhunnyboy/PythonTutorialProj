import datetime

"""
datetime比time高级了不少，可以理解为datetime基于time进行了封装，
提供了更为实用的函数，datetime模块的接口更直观，更容易调用

模块中的类：
datetime    同时有时间和日期
timedelta   主要用于时间的跨度
tzinfo      时区相关的
time        只关注时间
date        只关注日期

"""

# 获取当前时间
date1 = datetime.datetime.now()
print("date1 = ", date1)
print("date1 type = ", type(date1))

# 获取指定时间
date2 = datetime.datetime(2020, 2, 1, 10, 28, 30, 1234)
print("date2 = ", date2)

# 将时间转为字符串
date3 = date1.strftime("%y-%m-%d %X")
print("date3 = ", date3)
print("date3 type = ", type(date3))

# 将格式化字符串转为datetime对象
# 注意：转换的格式要与字符串一致
date4 = datetime.datetime.strptime(date3, "%y-%m-%d %X")
print("date4 = ", date4)
print("date4 type = ", type(date4))


date5 = datetime.datetime(2019, 2, 1, 10, 28, 30, 1234)
date6 = datetime.datetime.now()
date7 = date6 - date5
print("date7 = ", date7)
print("date7 type = ", type(date7))
# 间隔的天数
print("date7 days = ", date7.days)
# 间隔天数除外的秒数
print("date6 seconds = ", date7.seconds)
