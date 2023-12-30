# https://docs.sympy.org/latest/guides/custom-functions.html#custom-functions

from decimal import Decimal, ROUND_HALF_UP
from sympy import symbols, Function, Integer, Float 

x, y, a, b, c = symbols("x y a b c")

print('f = Function("f") と y = a + b + c を表示します')
f = Function("f")
y = a + b + c
print(f, type(f))
print(y, type(y))

print()
print("x と f(x) を表示します")
print(x, type(x))
print(f(x), type(f(x)))

def g(x):
    """ 完全に値を評価できる関数の時 """
    if x == 0:
        return 0
    else:
        return x + 1

print()
print("The Fully Evaluated Case の g(x) と g(1) を表示")
print(g(x), type(g(x)))
print(g(0), type(g(0)))

class nint(Function): # ninit 関数の定義
    """ Creating a Custom Function
     これは round 関数を使用しているので間違い """
    @classmethod
    def eval(cls, x, *args):
        # if x is an integer or float
        if isinstance(x, Integer) or isinstance(x, Float):
            return round(x)

print()
print("Createting a Custom Function の nint(x) nint(1.5) nint(1.4) nint(2.5) を表示")
print(nint(x), type(nint(x)))
print(nint(1.5), type(nint(1.5)))
print(nint(1.4), type(nint(1.4)))
print(nint(2.5), type(nint(2.5)))
print("round 関数は四捨五入じゃない")

class nint2(Function): # ninit 関数の定義 2 個目
    """ Creating a Custom Function
     これは 四捨五入 関数を使用している """
    @classmethod
    def eval(cls, x, *args):
        # if x is an integer or float
        if isinstance(x, Integer) or isinstance(x, Float):
            return Decimal(str(x)).quantize(Decimal("0"), ROUND_HALF_UP)

print()
print("nint2(x) nint2(1.5) nint2(1.4) nint2(2.5) を表示")
print(nint2(x), type(nint2(x)))
print(nint2(1.5), type(nint2(1.5)))
print(nint2(1.4), type(nint2(1.4)))
print(nint2(2.5), type(nint2(2.5)))

print()
print("引数を多くした場合 nint2(2.5 , 3)")
print(nint2(2.5, 3), type(nint2(2.5, 3)))

print()
print("数式を設定")
expr = 1 + nint( 5 + a * (2 + 3))
print(expr, type(expr))

print()
print("数式を設定 a に 1.5 を代入")
print(expr.subs(a, 1.5))

print()
print("数式を設定2")
expr = 1 + nint2( 5 + a * (2 + 3))
print(expr, type(expr))

print()
print("数式を設定2 a に 1.5 を代入")
print(expr.subs(a, 1.5))
