""" Python ではじめるアルゴリズム入門
伝統的なアルゴリズムで学ぶ定石と計算量
増井 敏克 緒
翔泳社 

第2章 基本的なプログラムから作ってみる
10 進数から 2 進数に変換する """

n = 18

def convert(n:int, base:int) -> str:
    """ 10 進数の数値 n を、base 進数の表記の文字列にして返します

    パラメーター
    ---
    n
        変更したい 10 進数
    base
        変更先の基数 """
    result = ""

    while n > 0:
        result = str(n % base) + result    # ← あまりを文字列の左側に追加していく
        n //= base                         # base で割った商を再度代入する

    return result

print(a := convert(n, 2))
assert int(a, 2) == n

print(a := convert(n, 3))
assert int(a, 3) == n

print(a := convert(n, 8))
assert int(a, 8) == n
