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
    messagebox.showinfo("お知らせ", "作業を開始してください")

#show_messagebox()
    
class Player:
    score = 0  # これはクラス変数ではないのか? クラス.変数名でアクセスする必要あり

p1 = Player()
p2 = Player()
print("値設定前、インスタンス変数")
print(F"プレイヤー1:{p1.score}点\n"
      F"プレイヤー2:{p2.score}点")

p1.score = 15   # これはインスタンス変数に代入していることになると推測
p2.score = 20   # 〃

print("値設定後、インスタンス変数、クラス変数")
print(F"プレイヤー1:{p1.score}点\n"
      F"プレイヤー2:{p2.score}点")
print(F"プレイヤー1:{Player.score}点\n"
      F"プレイヤー2:{Player.score}点")

class Dog:
    kind = "canine"

    def __init__(self, name) -> None:
        self.name = name

d = Dog("Fido")
e = Dog("Buddy")
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

d.kind = "d の種類変更した"

print(d.kind)
print(e.kind)
print(d.name)
print(e.name)