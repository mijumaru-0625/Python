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
    
x, y, z = symbols("x y z")

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

from sympy import pi, Integer, cos

class versin(Function):
    @classmethod
    def eval(cls, x):
        # if is an inter mulipleof pi, x/pi will cancel and be an Integer
        n = x / pi
        if isinstance(n, Integer):
            return 1 - (-1) ** n
        

print("Create a Custom Function")
print(versin(x))
print(isinstance(versin(x), versin))
print()

print("Defining Automatic Evaluation with eval()")
print(versin(pi))
print(versin(2 * pi))
print(versin(x * pi))
print()

class f(Function):
    @classmethod
    def eval(cls, x, y=1, *args):
        return None

print(f(1).args)
print(f(1, 2).args)
print(f(1, 2, 3).args)
print()

print(versin(x + y))