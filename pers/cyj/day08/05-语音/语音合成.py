# 系统客户端
import win32com.client
import time

speaker = win32com.client.Dispatch("SAPI.SPVOICE")

while True:
    time.sleep(1)
    speaker.Speak("Sunny is a handsome man")
