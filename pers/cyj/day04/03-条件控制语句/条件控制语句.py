# -*- coding: utf-8 -*-
"""
if语句
if-else语句

if-elif-else语句
格式：
if 表达式1:
    语句1
elif 表达式2:
    语句2
elif 表达式3:
    语句3
......
elif 表达式n:
    语句n
else: #可有可无
    语句e
逻辑：但程序执行到if-elif-else语句时，
首先计算“表达式1”的值，
如果“表达式1”的值为真，则执行“语句1”，执行完“语句1”，则跳过整个if-elif-else语句，
如果“表达式1”值为假，计算“表达式2”的值，
如果“表达式2”的值为真，则执行“语句2”，执行完“语句2”，则跳过整个if-elif-else语句，
如果“表达式2”值为假，计算“表达式3”的值，
如此下去直到某个表达式的值为真才停止，如果没有一个真的表达式，且有else语句，则执行“语句e"
"""
age = int(input("请输入您的年龄："))
if age < 0:
    print("娘胎里")
# 每个elif都是对它上面所有表达式的否定
elif age <= 3:
    print("婴儿")
elif age <= 6:
    print("儿童")
elif age <= 18:
    print("童年")
elif age <= 30:
    print("青年")
elif age <= 40:
    print("壮年")
elif age <= 50:
    print("中年")
elif age <= 100:
    print("老年")
elif age <= 150:
    print("老寿星")
else:
    print("老妖怪")
