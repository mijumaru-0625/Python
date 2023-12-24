"""
文字列を数式に変換するサンプルプログラムを検討
↓ 参考サイト
https://docs.sympy.org/latest/modules/parsing.html
https://docs.sympy.org/latest/guides/custom-functions.html#the-fully-symbolic-case

The Fully Symbolic Case
"""

from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import T
from sympy import Function

def parse_str_to_dict() -> dict:
    """  数式の文字列を左辺をキー、右辺を値として辞書に保存します """
    input_str = """
kinngaku = 998
zeiritu  = 0.1
kosuu    = 5
total1   = kinngaku * kosuu * (1 + zeiritu)
total2   = ShisyaGonyu(total1, -2)
tset_abs = abs(-5)
DNA_1    = 0.495
length   = 4.0 * DNA_1
"""

    print("入力文字列")
    print(input_str)
    print()

    lines = input_str.split("\n")
    print("行で分割")
    print(lines)
    print()

    lines = [line.split("=") for line in lines if "=" in line]
    print("=で分割")
    print(lines)
    print()

    lines = {params[0].strip(): params[1].strip() for params in lines if len(params) == 2}
    print("辞書形式に")
    print(lines)
    print()

    return lines

def parse_expr_test(lines: dict) -> None:
    """ 数式を評価するサンプルプログラム """
    print("local_dict を表示")
    local_dict = {"ShisyaGonyu": Function("ShisyaGonyu")} # ShisyaGonyu 関数を追加 
    print(local_dict)
    print()

    for k, v in lines.items():
        parse_result = parse_expr(v, local_dict, T[2:5])
        local_dict[k] = parse_result
        lines[k] = parse_result

    print("parse_expr 後に local_dict をもう一度表示")
    print(local_dict)
    print(local_dict["kinngaku"], type(local_dict["kinngaku"]))
    print()

    print("parse_expr 後に読み込み文字列をもう一度表示")
    print(lines)
    print()


lines = parse_str_to_dict() # 文字列→辞書に
parse_expr_test(lines)      # 左辺、右辺の辞書を評価します

for k, v in lines.items():
    print(k, v)
