"""
https://tkdocs.com/tutorial/concepts.html
Binding to Events
"""

from tkinter import *
from tkinter import ttk
root = Tk()
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight= 1)


l =ttk.Label(mainframe, text="Starting...", background="#FF0000")
# ラベル小さすぎ
l.grid(column=1, row=1, sticky=(N, W, E, S))
mainframe.rowconfigure(0, weight=5)
mainframe.columnconfigure(0, weight=5)
mainframe.rowconfigure(1, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=5)
mainframe.columnconfigure(2, weight=5)

l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
root.mainloop()