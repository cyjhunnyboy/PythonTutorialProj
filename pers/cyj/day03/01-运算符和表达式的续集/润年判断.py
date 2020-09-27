"""
从控制台输入一个年份，判断是否是润年
条件：能被4整除但是不能被100整除，或者能400整除
"""
year = int(input("请输入年份："))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("year = %d 是润年！" % year)
else:
    print("year = %d 不是润年！" % year)
