"""
https://docs.sympy.org/latest/guides/custom-functions.html#writing-custom-functions

The Fully Evaluated Case
"""

from sympy import symbols, Function

def f(x):
    if x == 0:
        return 0
    else:
        return x + 1
    
x = symbols("x")

print("The Fully Evaluated Case")
print(f(0))
print(f(1))
print(f(x))
print()

from sympy import Piecewise, Eq, pprint

f = Piecewise((0, Eq(x, 0)), (x + 1, True))
pprint(f, use_unicode=True)
print(f.subs(x, 0))
print(f.subs(x, 1))
print(f)
print()

class versin(Function):
    pass

print(versin(x))
print(isinstance(versin(x), versin))