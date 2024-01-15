""" Python で始めるアルゴリズム入門
6.3 ダイクストラ法
ヒープのライブラリを利用、ゴールを指定
p.227 リスト6.7 """

import heapq

def dijkstra(edges, num_v, goal):
    dist = [float("inf")] * num_v
    dist[0] = 0
    q = []# q は、コスト, 経路のリスト のリストでヒープソートしておく
    heapq.heappush(q, [0, [0]])

    while len(q) > 0:
        # ヒープソートされているキューから最小の経路を取り出し
        _, u = heapq.heappop(q) # 経路を u に代入
        last = u[-1]
        if last == goal:
            return u # 経路を返す

        # 各辺に対してコストを調べる
        for i in edges[last]:  # 取り出した頂点に接続する辺を順にループ
            if dist[i[0]] > dist[last] + i[1]:
                # 頂点までのコストが更新できれば更新
                dist[i[0]] = dist[last] + i[1]
                heapq.heappush(q, [dist[last] + i[1], u + [i[0]]])

    return []


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
print(dijkstra(edges, 7, 6))