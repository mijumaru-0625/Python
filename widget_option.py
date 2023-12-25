"""
https://tkdocs.com/tutorial/concepts.html
Configuration Options
"""

from tkinter import *
from tkinter import ttk
import pprint

root = Tk()
button = ttk.Button(root, text="Hello", command="buttonpressed")
button.grid()

print("text オプションの現在の値を確認")
print(button["text"])
print()

print("text オプションの値を変更")
button["text"] = "goodbye"
print(button["text"])
print()

print("text オプションの値を変更、方法2")
button.configure(text="byebye")
print(button["text"])
print()

print("text オプションのすべての値を表示")
print(button.configure("text"))
print()

print("ボタンのすべてのオプションを表示")
pprint.pprint(button.configure())