""" p.191 ライブラリを使う
リスト 5.10 """

import heapq

def heap_sort(array):
    h = array.copy()
    heapq.heapify(h) # ヒープを構成
    return [heapq.heappop(h) for _ in range(len(array))] # 取り出しながらソート済のリストを作成


data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

print(heap_sort(data))
