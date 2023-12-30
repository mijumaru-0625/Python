"""
https://docs.sympy.org/latest/tutorials/intro-tutorial/manipulation.html

Advanced Expression Manipulation のページを実際に
ソースコードを入力して確認しました

sympy_test6.py の続き
"""
# Prevent expression evaluation

from sympy import Add
from sympy.abc import x, y, z

print(x + x)

print(Add(x, x))

print(Add(x, x, evaluate=False))

print("\nsympify を使用")
from sympy import sympify
print(sympify("x + x", evaluate=False))

print("\nparse_expr を使用")
from sympy.parsing.sympy_parser import parse_expr
print(parse_expr("x + x"))
print(parse_expr("x + x", evaluate=False))

expr = Add(x, x, evaluate=False)
print(expr)
print(expr + x)

print("\nUneveluatedExpr 使用")
from sympy import UnevaluatedExpr
expr = x + UnevaluatedExpr(x)
print(expr)
print(x + expr)

print((x + expr).doit())

