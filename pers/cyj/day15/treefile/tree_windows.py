import tkinter
from tkinter import ttk


class TreeWindow(tkinter.Frame):

    def __init__(self, master, path):
        frame = tkinter.Frame(master)
        frame.pack()

        self.tree = ttk.Treeview(frame)
        self.tree.pack()

        root = self.tree.insert("", "end", text = path, open=True)
