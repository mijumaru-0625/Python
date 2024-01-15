""" Python で始めるアルゴリズム入門
6.4 A* アルゴリズム
p.233 リスト6.8 """

import pprint

# 図6.12 のコストの推定値、順に頂点 S, A, B, ..., L, M の G までの距離
nodes = [
    10, 14, 10, 10, 9, 9, 5, 0, 9, 8, 6, 4, 7, 3
]

# 図6.12 の辺のリスト、終点とコストのリスト
# 終点のインデックス 0:S, 1:A, 2:B, ...
edges = [
    [["D", 1], ["E", 1]],                   # 頂点 S に接続する辺の終点とコスト
    [["B", 12], ["C", 4], ["D", 15]],       # 頂点 A
    [["A", 12], ["I", 2], ["K", 6]],        # 頂点 B
    [["A", 4], ["E", 3], ["H", 3]],         # 頂点 C
    [["A", 15], ["S", 1], ["F", 6]],        # 頂点 D
    [["S", 1], ["C", 3], ["F", 4]],         # 頂点 E
    [["D", 6], ["E", 4], ["J", 1]],         # 頂点 F
    [["K", 4], ["M", 5]],                   # 頂点 G
    [["C", 3], ["I", 1], ["J", 5]],         # 頂点 H
    [["B", 2], ["H", 1], ["L", 1]],         # 頂点 I
    [["F", 1], ["H", 5], ["M", 3]],         # 頂点 J
    [["B", 6], ["G", 4], ["L", 5]],         # 頂点 K
    [["I", 1], ["K", 5], ["M", 6]],         # 頂点 L
    [["G", 5], ["J", 3], ["L", 6]],         # 頂点 M、テキストでは M → J、M → L のコストが間違っている
                                            # が、M → G に向かえば済みなので不具合は発生していない
]

# データ変換前の確認
#pprint.pprint(edges)

# データ変換
points = "SABCDEFGHIJKLM"
point_to_index = {s: i for i, s in enumerate(points)}
index_to_point = {v: k for k, v in point_to_index.items()}

for edge in edges:
    for e in edge:
        e[0] = point_to_index[e[0]]        


# データ変換後の確認
#pprint.pprint(edges)

import heapq

def aster(edges, nodes, goal):
    dist = [float("inf")] * len(nodes)
    dist[0] = 0
    q = []
    heapq.heappush(q, [0, [0]])

    while len(q) > 0:
        _, u = heapq.heappop(q)
        last = u[-1]
        if last == goal:
            return u
        
        for i in edges[last]:
            if dist[i[0]] > dist[last] + i[1]:
                dist[i[0]] = dist[last] + i[1]
                heapq.heappush(q, [dist[last] + i[1] + nodes[i[0]], u + [i[0]]])

        
    return []


print(ret:=aster(edges, nodes, 7))
print([index_to_point[i] for i in ret])
