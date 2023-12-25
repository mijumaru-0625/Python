"""
https://tkdocs.com/tutorial/firstexample.html
"""

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)

        print_hierarchy(root)
    except ValueError:
        pass

root = Tk()
root.title("メートルに換算")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# ウィンドウのリサイズに追従するようにできた
mainframe.columnconfigure(2, weight=1) # 真ん中の列が横に伸びる
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
#mainframe.rowconfigure(3, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="計算", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="フィート").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="は、次と同じです。").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="[m]").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)

print_hierarchy(root)

root.mainloop()