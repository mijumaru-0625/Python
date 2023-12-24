""" Python ではじめるアルゴリズム入門
伝統的なアルゴリズムで学ぶ定石と計算量
増井 敏克 緒
翔泳社 

https://qiita.com/sudo00/items/2b2eec07d3099b5ad664

文字コード  意味
\033[0J     カーソル位置から画面右下まで消去
\033[1J     画面左上からカーソル位置まで消去
\033[2J     画面クリア
\033[0K     カーソル位置から同じ行の右側消去
\033[1K     カーソル位置から同じ行の左側消去
\033[2K     カーソルのある１行の消去
\033[nA     カーソルをn行上へ移動
\033[nB     カーソルをn行下へ移動
\033[nC     カーソルをn桁右へ移動 右端で停止
\033[nD     カーソルをn桁左へ移動 左端で停止
\033[r;nH	カーソルをr行、n桁目へ移動

"""

import time


# 入力データ準備
maze_str = """
############
#S  #      #
# #   ## # #
# ## #   # #
#   #  ## ##
###  # #   #
#   # #  #G#
# #    #  ##
#  # #  #  #
# # # #  # #
#      #   #
############
"""

# テキストの状態に格納
maze = []
for line in maze_str.split("\n"):
    if line.strip() == "":
        continue

    row = []
    for s in list(line):
        if s == "#":
            row.append(9)
        elif s == "G":
            row.append(1)
        else:
            row.append(0)


    maze.append(row)

import pprint

def print_maze():
    for line in maze:
        for c in line:
            if c == 9:
                print("＃", end="")
            elif c == 1:
                print("Ｇ", end="")
            elif c == 2:
                print("・", end="")
            else:
                print("　", end="")
        
        print()

print_maze()

print()
print("迷路の探索（番兵）右手法による深さ優先探索")

# 右手法での移動方向（下、右、上、左）をセット
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# スタート位置(x 座標、y 座標、移動回数、方向)をセット
x, y, depth, d = 1, 1, 0, 0


while maze[y][x] != 1:
    # 探索済みとしてセット
    maze[y][x] = 2

    print(str(depth) + " ")
    print_maze()
    time.sleep(0.5)
    print(F"\033[{len(maze) + 2}A")

    # 右手法で探索
    for i in range(len(dir)):
        # 進行方向から右側に順に探す
        j = (d + i - 1) % len(dir) # 移動方向の個数で割ってあまりを求めることで、次の方向を求める
        if maze[y + dir[j][1]][x + dir[j][0]] < 2: # 次の方向を決める
            # 未訪問の場合は進めて移動回数を増やす
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth += 1
            break

        elif maze[y + dir[j][1]][x + dir[j][0]] == 2:
            # 訪問済みの場合は進めて移動回数を減らす
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth -= 1
            break


print(str(depth) + " ")
print("\n" * len(maze))