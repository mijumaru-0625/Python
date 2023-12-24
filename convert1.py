""" Python ではじめるアルゴリズム入門
伝統的なアルゴリズムで学ぶ定石と計算量
増井 敏克 緒
翔泳社 
"""

n = 18

def convert_from_decimal(n:int, base:int) -> str:
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


print(nstr := convert_from_decimal(n, 2))
assert int(nstr, 2) == n

# 2 進数から 10 進数に変換する

result = 0
for i in range(len(nstr)):
    result += int(nstr[i]) * (2 ** (len(nstr) - i - 1))

print(result)
assert result == n

print()
print("bin 関数で 10 進数から 2 進数に変換可能")
print(bin(n))

print()
print("int 関数の第 2 引数に 2 を指定することで、2 進数の文字列から 10 進数に変換可能")
print(int(nstr, 2))

print()
print("先頭に 0b とつけることで 2 進数のリテラルとして扱える")
a = 0b10010
print(a)