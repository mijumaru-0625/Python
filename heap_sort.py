""" p.189 汎用的な実装を作る
リスト 5.9 """

def heapify(data, i):
    left = 2 * i + 1    # 左下の位置
    right = 2 * i + 2   # 右下の位置
    size = len(data) - 1
    min = i

    if left <= size and data[min] > data[left]: # 左下の方が小さい時
        min = left

    if right <= size and data[min] > data[right]:   # 右下の方が小さい時
        min = right

    if min != i:    # 交換が発生する時
        data[i], data[min] = data[min], data[i]
        heapify(data, min)  # ヒープを再構成


data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# ヒープを構成
for i in reversed(range(len(data) // 2)):  # 葉ノード以外を処理
    heapify(data, i)


# ソートを実行
sorted_data = []
for _ in range(len(data)):
    data[0], data[-1] = data[-1], data[0]   # 最後のノードと先頭を入れ替え
    sorted_data.append(data.pop())          # 最後のノードを取り出してソート済みにする
    heapify(data, 0)                        # ヒープを再構成


print(sorted_data)
