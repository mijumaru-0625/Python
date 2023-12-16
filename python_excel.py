"""
今すぐ使える
かんたん biz
Python
  x
Excel 自動処理
ビジネス活用
大全
"""

import tkinter
from tkinter import messagebox

def show_messagebox():
    """ メッセージボックスを表示する """
    #root = tkinter.Tk()    # この行不要だった?
    #root.withdraw()        # この行不要だった?
    print(messagebox.showinfo("お知らせ", "作業を開始してください"))
    print(messagebox.showwarning("警告", "作業を開始してください"))
    print(messagebox.showerror("エラー", "作業を開始してください"))
    ret = messagebox.askquestion("質問", "はい、いいえで答えて") # 戻り値が文字列の "yes" または "no"
    print(ret, type(ret))
    print(messagebox.askokcancel("質問", "OK、キャンセルで答えて"))
    print(messagebox.askretrycancel("質問", "再試行、キャンセルで答えて"))
    print(messagebox.askyesno("質問", "はい、いいえで答えて"))
    print(messagebox.askyesnocancel("質問", "はい、いいえ、キャンセルで答えて"))

#show_messagebox()

from tkinter import simpledialog

root = tkinter.Tk()    # この行不要だった?
root.withdraw()        # この行不要だった?
kosu = simpledialog.askinteger("購入数", "購入したい個数を入力してください")
if kosu:
    kingaku = kosu * 120
    messagebox.showinfo("金額", F"購入金額:{kingaku}円")
