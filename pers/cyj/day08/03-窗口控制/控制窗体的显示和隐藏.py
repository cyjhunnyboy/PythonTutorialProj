import win32con
import win32gui
import time

while True:

    # 找出窗体的编号
    qqWin = win32gui.FindWindow("TXGuiFoundation", "QQ")

    # 隐藏窗体
    win32gui.ShowWindow(qqWin, win32con.SW_HIDE)

    time.sleep(2)

    # 显示窗体
    win32gui.ShowWindow(qqWin, win32con.SW_SHOW)

    time.sleep(2)
