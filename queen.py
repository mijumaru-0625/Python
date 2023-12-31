"""
8 クイーン問題
p.143
"""

import copy

N = 11

# 斜めのチェック
def check(y_index_of_next_Q:int, col:list) -> bool:
    """ 各列のどの行に Q が配置されているかのリスト col
    において、次の列の Q の配置場所として y_index_of_next_Q
    が配置可能かどうかを確認します。
    配置可能な時 True を返します。
    """
    # 配置済みの行を逆順に調べる
    for i, y_index in enumerate(reversed(col)):
        #                             vv 左下のチェック　　　　　　　　　　　　　　 vv 左上のチェック
        if (y_index_of_next_Q + i + 1 == y_index) or (y_index_of_next_Q - i - 1 == y_index): # 左上と左下にあるか
            return False
        
    return True
        

def search(col:list):
    """ 引数 col には各列のどの行に Q が配置されるかを格納します。
    配置される場所は 0 ～ 7 = N - 1 の値
    """
    global g_list_count

    if len(col) == N:   # すべて配置できれば出力
        y_index_list_of_Q.append(copy.copy(col))
        return
    
    for i in range(N):
        if i not in col: # 同じ行は使わない
            if check(i, col):
                col.append(i)
                search(col) # 再帰的に探索する
                col.pop()
                

y_index_list_of_Q = []
search([])

# 重複のチェック
def check_duplicate(currnet_index:int, rotate_angle:int = 0, currnet_y_index:list = None) -> bool:
    """ 重複したら False を返します """

    if rotate_angle >= 360:
        return True

    msg = ""
    if rotate_angle != 0:
        msg = F"{rotate_angle}°回転"

    if currnet_y_index is None:
        currnet_y_index = copy.copy(y_index_list_of_Q[currnet_index])
    else:
        for i in range(currnet_index):
            if y_index_list_of_Q[i] == currnet_y_index:
                print(F" {i}と{msg}で重複")
                return False


    check_list = list(reversed(currnet_y_index)) # 逆順に並べ替え、左右反転

    for i in range(currnet_index):
        if y_index_list_of_Q[i] == check_list:
            print(F" {i}と{msg}左右反転で重複")
            return False
        
    check_list = [N - 1 - i for i in currnet_y_index] # 上下反転

    for i in range(currnet_index):
        if y_index_list_of_Q[i] == check_list:
            print(F" {i}と{msg}上下反転で重複")
            return False

    x_y_index_list = [(x, y) for x, y in enumerate(currnet_y_index)]
    rotate_x_y_index_list = [(N - 1 - y, x) for x, y in x_y_index_list]
    rotate_x_y_index_dict = {x: y for x, y in rotate_x_y_index_list}
    rotate_y_index_list = [rotate_x_y_index_dict[x] for x in range(N)]

    return check_duplicate(currnet_index, rotate_angle + 90, rotate_y_index_list)


# 確認
check_count = 0
for i, y_index_of_Q in enumerate(y_index_list_of_Q):
    print(i, y_index_of_Q, end="")

    if not check_duplicate(i):
        continue

    print()
    check_count += 1


print(F"重複なしは、{check_count} 個")