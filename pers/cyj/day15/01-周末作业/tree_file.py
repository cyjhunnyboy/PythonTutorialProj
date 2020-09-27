import tkinter
import os
from pers.cyj.day15.treefile.tree_windows import TreeWindow

win = tkinter.Tk()
win.title("File Tree")
win.geometry("900x400+500+200")

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))))

print(path)

treeWin = TreeWindow(win, path)

win.mainloop()
