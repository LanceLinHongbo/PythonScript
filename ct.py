import sys
from pyautogui import typewrite
import time
#剪切时间线,需配合更改键盘快捷键“shift+down”选择“时间线标记”变为pagedown
def ctl(x):
    time.sleep(5)
    for i in range(x):
        typewrite(["pgdn"],0.1)
        typewrite(["b"],0.1)
#给已经剪切的静音片段加标签，x是当前时间线片段数量除以2加1，需配合更改键盘快捷键选择“时间线上的片段标记”变为down
def adm(x):
    time.sleep(5)
    typewrite(['down','up','m'],0.20)
    for i in range(x):
            typewrite(['down','down','m'],0.20)
print()
print("ctl(x):剪切时间线,x是时间线标记的数量")
print()
print("需配合更改键盘快捷键选择“时间线标记”设置为pagedown")
print()
print("adm(x):给已经剪切的静音片段加标签，x是当前时间线片段数量除以2")
print()
print("需配合键盘快捷键选择“片段标记”设置为down")
print()
