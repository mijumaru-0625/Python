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
print("迷路の探索（番兵）深さ優先探索")

def search(x, y, depth):
    """ 深さ優先探索 """
    # ゴールに着くと終了
    if maze[y][x] == 1:
        print(depth)
        print_maze()
        exit() # 再帰呼び出しとなっているので　return ではだめ
    
    # 探索済みとしてセット
    maze[y][x] = 2

    print(str(depth) + " ")
    print_maze()
    time.sleep(0.2)
    print(F"\033[{len(maze) + 2}A")

    # 上下左右を探索
    if maze[y - 1][x] < 2:
        search(x, y - 1, depth + 1)     # 移動回数を増やして上を探索

    if maze[y + 1][x] < 2:
        search(x, y + 1, depth + 1)     # 移動回数を増やして下を探索
        
    if maze[y][x - 1] < 2:
        search(x - 1, y, depth + 1)     # 移動回数を増やして左を探索

    if maze[y][x + 1] < 2:
        search(x + 1, y, depth + 1)     # 移動回数を増やして右を探索



# スタート位置から開始
search(1, 1, 0)