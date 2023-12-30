"""
https://docs.sympy.org/latest/tutorials/intro-tutorial/manipulation.html

Advanced Expression Manipulation のページを実際に
ソースコードを入力して確認しました

sympy_test7.py の続き
"""

from sympy import *
from sympy.abc import x, y, z

uexpr = UnevaluatedExpr(S.One*5/7)*UnevaluatedExpr(S.One*3/4)
print(uexpr)
print(x * UnevaluatedExpr(1/x))

expr1 = UnevaluatedExpr(x + x)
print(expr1)

expr2 = sympify("x + x", evaluate=False)
print(expr2)

print(UnevaluatedExpr(sympify("x + x", evaluate=False)) + y)