"""
https://docs.sympy.org/latest/tutorials/intro-tutorial/manipulation.html

Advanced Expression Manipulation のページを実際に
ソースコードを入力して確認しました
"""

# Understanding Expression Trees
from sympy import *
x, y, z = symbols("x y z")

expr = x**2 + x*y
print(srepr(expr))

print(srepr(x**2))

print(Pow(x, 2))

print(type(2))

print(type(sympify(2)))
print(type(sympify("2")))

print(srepr(x*y))

print(Mul(x, y))

print(Add(Pow(x, 2), Mul(x, y)))

expr = sin(x*y)/2 - x**2 + 1/y
print(srepr(expr))

print(srepr(x - y))

expr = x/y
print(srepr(expr))

print(1 + x)

x = Symbol("x", commutative=False)
print(1 + x)

x = Symbol("x")
print(1 + x)

# Recursing through an Expression Tree
# func
expr = Add(x, x)
print(expr.func)
print(expr)

print(Integer(2).func)
print(isinstance(Integer(2), Integer))
print(Integer(0).func)
print(isinstance(Integer(0), Integer))
print(Integer(-1).func)
print(isinstance(Integer(-1), Integer))

# args
expr = 3*y**2*x
print(expr)
print(expr.func)
print(expr.args)

print(expr.func(*expr.args))
print(expr == expr.func(*expr.args))

expr = y**2 * 3 * x
print(expr.args)

print(expr.args[2])

print(expr.args[2].args)

print(y.args)
print(Integer(2).args)
print(y.func)
print(Integer(2).func)

# Walking the Tree
def pre(expr):
    print(expr)
    for arg in expr.args:
        pre(arg)

expr = x*y + 1
pre(expr)

print("\npreoder_travasal 関数を使用")
for arg in preorder_traversal(expr):
    print(arg)

print("\npostoder_travasal 関数を使用")
for arg in postorder_traversal(expr):
    print(arg)