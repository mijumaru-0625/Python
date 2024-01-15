""" Python で始めるアルゴリズム入門
6.3 ダイクストラ法
ヒープによる優先度付きキューを実装する
p.224 リスト6.5 """

def min_heapify(data, i):
    left = 2 * i + 1
    right = 2 * i + 2

    min = i
    if left < len(data) and data[min][0] > data[left][0]:
        min = left # 左の方が小さい場合は、最小値の位置に左をセット
    
    if right < len(data) and data[min][0] > data[right][0]:
        min = right # 右の方が小さく場合は、最小値の位置に右をセット

    if min != i:
        data[i], data[min] = data[min], data[i]
        min_heapify(data, min)


def dijkstra(edges, num_v):
    dist = [float("inf")] * num_v
    dist[0] = 0
    q = [[0, 0]] # q は、コスト, 位置 のリストでヒープソートしておく

    while len(q) > 0:
        # ヒープソートされているキューから最小の要素を取り出し
        q[0], q[-1] = q[-1], q[0]
        _, u = q.pop()  # 位置を u に代入
        # キューを再構成
        min_heapify(q, 0)

        # 各辺に対してコストを調べる
        for i in edges[u]:  # 取り出した頂点に接続する辺を順にループ
            if dist[i[0]] > dist[u] + i[1]:
                # 頂点までのコストが更新できれば更新
                dist[i[0]] = dist[u] + i[1]
                q.append([dist[u] + i[1], i[0]])    # コスト、位置を q に追加
                j = len(q) - 1
                while (j > 0) and (q[(j - 1) // 2] > q[j]):
                    q[(j - 1) // 2], q[j] = q[j], q[(j - 1) // 2]
                    j = (j - 1) // 2

    return dist


# 辺のリスト、各頂点に接続する辺について接続先の頂点（終点）とコストのリスト
edges = [
    [[1, 4], [2, 3]],           # 頂点 A に接続する辺の終点とコストのリスト
    [[2, 1], [3, 1], [4, 5]],   # 頂点 B
    [[5, 2]],                   # 頂点 C　　　　　　　　　　　　　　　　　　、辺には向きがあるようだ
    [[4, 3]],                   # 頂点 D
    [[6, 2]],                   # 頂点 E
    [[4, 1], [6, 4]],           # 頂点 F
    []                          # 頂点 G
]
print(dijkstra(edges, 7))