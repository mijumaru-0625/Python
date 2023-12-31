"""
https://docs.sympy.org/latest/tutorials/intro-tutorial/manipulation.html

Advanced Expression Manipulation のページを実際に
ソースコードを入力して確認しました
"""

# Understanding Expression Trees
from sympy import Symbol, Function, UnevaluatedExpr
from sympy.parsing.sympy_parser import parse_expr, T

x = Symbol("x")
y = Symbol("y")

local_dict = {}
local_dict["x"] = x
local_dict["y"] = y    
local_dict["nint"] = Function("nint")
local_dict["round"] = Function("round")


# Sympy を利用して式を評価すると簡単な関数は数値に変換してしまうことが判明した。
# 元の数式が消えてしまう
expr_str = "x*y + 1 + 2 + 3 + nint(5.5) + round(5.5, 2)"
expr = parse_expr(expr_str, local_dict, T[2:5] , evaluate=False)
expr_str2 = str(expr)


print(F"expr = {expr}")
print(F"expr_str2 = {expr_str2}")
print("式に変換後は順番が変わる。どうしようもないのか?")
