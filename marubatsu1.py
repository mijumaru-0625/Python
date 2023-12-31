""" p.157 リスト4.18 3 目並べ """


def print_maru_batsu(p1, p2):
    """ 訳が分からないので盤面を表示します """
    board_str = """
　：　：　
－＋－＋－
　：　：　
－＋－＋－
　：　：　"""
    board_str_list = list(board_str)
    board_str_index_list = [i for i, s in enumerate(board_str_list) if s == "\u3000"]
    left_top = 0b100000000
    board_str_index_dict = {left_top >> i: board_str_index_list[i] for i in range(9)}

    if p1_is_maru:
        mark_p1 = "〇" 
        mark_p2 = "Ｘ"
    else:
        mark_p1 = "Ｘ"
        mark_p2 = "〇" 

    for k, v in board_str_index_dict.items():
        if k & p1:
            board_str_list[v] = mark_p1

        if k & p2:
            board_str_list[v] = mark_p2

    print("".join(board_str_list))


goal = [
    0b111000000, 0b000111000, 0b000000111,
    0b100100100, 0b010010010, 0b001001001,
    0b100010001, 0b001010100
]

# 3 つ並んだか判定
def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
        
    return False


# ミニマックス法
def minmax(p1, p2, turn):
    if check(p2):
        if turn:    # 自分の手番の時は勝ち
            return 1
        else:       # 相手の手番の時は負け
            return -1
        
    board = p1 | p2
    if board == 0b111111111: # すべて置いたら引き分けで終了
        return 0
    
    w = [i for i in range(9) if (board & (1 << i)) == 0]

    if turn: # 自分の手番の時は最小値を選ぶ
        return min([minmax(p2, p1 | (1 << i), not turn) for i in w])
    else:
        return max([minmax(p2, p1 | (1 << i), not turn) for i in w])


# 交互に置く
def play(p1, p2, turn):
    if check(p2): # 3 つ並んでいたら出力して終了
        print("勝負あり", [bin(p1), bin(p2)])
        return
    
    board = p1 | p2
    if board == 0b111111111: # すべて置いたら引き分けで終了
        print("引き分け", [bin(p1), bin(p2)])
        return

    # 置ける場所を探す
    w = [i for i in range(9) if (board & (1 << i)) == 0]
    # 各場所に置いた時の評価値を調べる
    r = [minmax(p2, p1 | (1 << i), True) for i in w]
    # 評価値が一番高い場所を取得する
    j = w[r.index(max(r))]
    
    p1 = p1 | (1 << j)
    print_maru_batsu(p1, p2)

    global p1_is_maru
    p1_is_maru = not p1_is_maru
    play(p2, p1, not turn)  # 手番を入れ替えて次を探す、turn は使っていないと思う


p1_is_maru = True
play(0, 0, True)

