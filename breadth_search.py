""" Python ではじめるアルゴリズム入門
伝統的なアルゴリズムで学ぶ定石と計算量
増井 敏克 緒
翔泳社 
4.3 木構造での探索
幅優先探索
"""

tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14],
        [], [], [], [], [], [], [], []]

print("幅優先探索でめぐっているノードを表示します")
data = [0]
while len(data) > 0:
    pos = data.pop(0)  # 先頭からとりだし
    print(pos, end=" ")
    for i in tree[pos]:
        data.append(i)  # 末尾に追加

print("\n")

def search(pos):
    """ 深さ方向探索 行きがけ順 """
    print(pos, end=" ")     # 配下のノードを調べる前に出力
    for i in tree[pos]:     # 配下のノードを調べる
        search(i)           # 再帰的に探索


print("深さ方向探索 行きがけ順 のめぐっているノードを表示します")
search(0)
print("\n")

def search(pos):  # 同じ関数名にしても動作するんだ !!!
    """ 深さ方向探索 帰りがけ順 """
    for i in tree[pos]:     # 配下のノードを調べる
        search(i)           # 再帰的に探索

    print(pos, end=" ")     # 配下のノードを調べた後に出力


print("深さ方向探索 帰りがけ順 のめぐっているノードを表示します")
search(0)
print("\n")

def search(pos):
    """ 深さ方向探索 通りがけ順
    左のノードの後に出力としている """
    if len(tree[pos]) >= 1:     # 子がある時
        search(tree[pos][0])
        print(pos, end=" ")     # 子（左のノード）を調べた後に出力
        if len(tree[pos]) >= 2:
            for pos_to_search in tree[pos][1:]:
                search(pos_to_search)

    else:                       # 子がないの時
        print(pos, end=" ")     # 出力


print("深さ方向探索 通りがけ順 のめぐっているノードを表示します")
search(0)
print("\n")

print("深さ方向探索 帰りがけ逆順 ループで実装 のめぐっているノードを表示します")
data = [0]
while len(data) > 0:
    pos = data.pop()    # 末尾から取り出し
    print(pos, end=" ")
    for i in tree[pos]:
        data.append(i)  # 末尾に追加
