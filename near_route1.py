""" p.212 リスト6.2 メモ化 """

import functools

M, N = 6, 5

# Python では以下の 1 行を追加するだけで再帰処理をメモ化できる
@functools.lru_cache(maxsize=None)
def search(m, n):
    if (m == 0) or (n == 0):
        return 1
    
    return search(m - 1, n) + search(m, n - 1)

print(search(M, N))