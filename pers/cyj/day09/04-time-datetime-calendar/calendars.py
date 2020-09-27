import calendar

"""
日历模块使用

"""

# 返回指定某年某月的日历
print(calendar.month(2020, 1))

# 返回指定年份的日历
print(calendar.calendar(2020))

# 判断是否是润年，是返回True，否则返回False
print(calendar.isleap(2020))

# 返回某个月的weekday的第一天和这个月所有的天数
print(calendar.monthrange(2020, 3))

# 返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2020, 3))
