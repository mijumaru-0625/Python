"""
8 クイーン問題
p.143
"""

N = 8

# 斜めのチェック
def check(x, col):
    # 配置済みの行を逆順に調べる
    for i, row in enumerate(reversed(col)):
        if (x + i + 1 == row) or (x - i - 1 == row):
            return False
        
    return True
        

def search(col):
    """ 引数 col には各列のどの行に Q が配置されるかを格納します。
    配置される場所は 0 ～ 7 = N - 1 の値
    """
    global g_list_count

    if len(col) == N:   # すべて配置できれば出力
        g_list_count += 1
        print(g_list_count, col)
        return
    
    for i in range(N):
        if i not in col: # 同じ行は使わない
            if check(i, col):
                col.append(i)
                search(col) # 再帰的に探索する
                col.pop()
                

g_list_count = 0
search([])