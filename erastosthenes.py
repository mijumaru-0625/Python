""" Python ではじめるアルゴリズム入門
伝統的なアルゴリズムで学ぶ定石と計算量
増井 敏克 緒
翔泳社
2.5 素数を判定する 
高速に素数を求める方法を考える
エラスとてネスの篩
"""

import math
import time

def get_prime(n):
    if n <= 1:
        return []
    
    prime = [2]
    limit = int(math.sqrt(n))

    # 基数のリストの作成
    data = [i + 1 for i in range(2, n, 2)]
    while limit >= data[0]:
        prime.append(data[0])
        # 割り切れない数だけを取り出す
        data = [j for j in data if j % data[0] != 0]

    return prime + data

start_time = time.perf_counter_ns()
prime_list = get_prime(100000)
end_time = time.perf_counter_ns()

print(len(prime_list))
delta = end_time - start_time
print(F"処理にかかった時間[ms] : {delta / 1000 / 1000}")