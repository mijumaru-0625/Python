""" Python ではじめるアルゴリズム入門
伝統的なアルゴリズムで学ぶ定石と計算量
増井 敏克 緒
翔泳社
2.6 フィボナッチ数列を作る
"""

import time

def fibonacci(n):
    """ 再帰 を利用したフィボナッチ数列 
    この方法ではすごく時間がかかる。同じ計算を何度もしている。    
    """
    if (n == 1) or (n == 2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


start_time = time.perf_counter_ns()
print(fibonacci(30))
end_time = time.perf_counter_ns()
delta = end_time - start_time
print(F"fibonacci  処理にかかった時間[ms] : {delta / 1000 / 1000}")

# この利用方法だとグローバル変数を関数内で利用できる
memo = {1: 1, 2: 1} # 辞書に終了条件の値を入れる
                    
def fibonacci2(n):
    """ 再帰 + メモを利用したフィボナッチ数列 """
    if n in memo:
        return memo[n] # 辞書に登録されていれば、その値を返す
    
    memo[n] = fibonacci2(n - 2) + fibonacci2(n - 1)
    return memo[n]

start_time = time.perf_counter_ns()
print(fibonacci2(30))
end_time = time.perf_counter_ns()
delta = end_time - start_time
print(F"fibonacci2 処理にかかった時間[ms] : {delta / 1000 / 1000}") # 早い、びっくり

def fibonacci3(n):
    """ ループ、リストを利用したフィボナッチ数列 """
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])

    return fib[n - 1]

start_time = time.perf_counter_ns()
print(fibonacci3(30))
end_time = time.perf_counter_ns()
delta = end_time - start_time
print(F"fibonacci3 処理にかかった時間[ms] : {delta / 1000 / 1000}") # 早い、リストを利用する方法が普通かな

