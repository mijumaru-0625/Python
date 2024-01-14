""" Python で始めるアルゴリズム入門
6.3 ダイクストラ法
p.222 リスト6.4 """

def dijkstra(edges, num_v):
    dist = [float("inf")] * num_v
    dist[0] = 0
    q = [i for i in range(num_v)]

    while len(q) > 0:
        # 最もコストが小さい頂点を探す
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i       # コストが小さい頂点を見つけること更新

        # 最もコストが小さい頂点を取り出す
        u = q.pop(q.index(r))
        for i in edges[u]:  # 取り出した頂点に接続する辺を順にループ
            if dist[i[0]] > dist[u] + i[1]:
                # 頂点までのコストが更新できれば更新
                dist[i[0]] = dist[u] + i[1]

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