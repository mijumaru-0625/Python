""" Python ではじめるアルゴリズム入門
伝統的なアルゴリズムで学ぶ定石と計算量
増井 敏克 緒
翔泳社
2.5 素数を判定する 
"""

import math # ← 平方根を求めるのに使う数学モジュールを読み込む
import time

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:      # 割り切れるか判定
            return False    # 割り切れれば素数ではない
    
    return True             # いずれの数でも割り切れなかった時は素数

prime_list = []

start_time = time.perf_counter_ns()
for i in range(100000):
    if is_prime(i):
        prime_list.append(i)

end_time = time.perf_counter_ns()

print(len(prime_list))
delta = end_time - start_time
print(F"処理にかかった時間[ms] : {delta / 1000 / 1000}")