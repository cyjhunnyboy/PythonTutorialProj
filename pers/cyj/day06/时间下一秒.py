timeStr = input("请输入时间字符串：")

# 12:23:33
timeList = timeStr.split(":")

hour = int(timeList[0])
minute = int(timeList[1])
second = int(timeList[2])


second += 1

if second == 60:
    minute += 1
    second = 0
    if minute == 60:
        hour += 1
        minute = 0
        if hour == 24:
            hour = 0

print("%.2d:%.2d:%.2d" % (hour, minute, second))
