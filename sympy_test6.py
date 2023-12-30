"""
https://docs.sympy.org/latest/tutorials/intro-tutorial/manipulation.html

Advanced Expression Manipulation のページを実際に
ソースコードを入力して確認しました
"""

# Understanding Expression Trees
from sympy import Symbol, Function
from sympy.parsing.sympy_parser import parse_expr, T

x = Symbol("x")
y = Symbol("y")

local_dict = {}
local_dict["x"] = x
local_dict["y"] = y

# 計算のみ実行する自作関数
def func_abc(x):
    return abs(x) + 1


class func_def(Function):
    @classmethod
    def eval(cls, x):
        pass

    # def _eval_evalf(self, prec):
    #     return (abs(x) - 1)._eval_evalf(prec)
    

local_dict["func_abc"] = globals()["func_abc"]
local_dict["func_def"] = globals()["func_def"]

# Walking the Tree
def pre(expr):
    print(expr)
    for arg in expr.args:
        pre(arg)

# Sympy を利用して式を評価すると簡単な関数は数値に変換してしまうことが判明した。
# 元の数式が消えてしまう
expr = parse_expr("x*y + 1 + abs(-3) + func_abc(-5.5) + func_def(4.5)", local_dict, T[2:5] , evaluate=False)
print(F"expr = {expr}")
#pre(expr)

print("x = 1、y = 1 を与えて計算", expr.evalf(subs={x: 1, y: 1}))