# https://docs.sympy.org/latest/guides/custom-functions.html#custom-functions

from sympy import symbols, Function, Integer, Float 

x, y, a, b, c = symbols("x y a b c")

f = Function('f')
y = a + b + c

print(y)

print(x, type(x))
print(f(x), type(f(x)))

def myf(x):
    if x == 0:
        return 0
    else:
        return x + 1
    
print(myf(x), type(myf(x)))

class nint(Function): # ninit 関数の定義
    @classmethod
    def eval(cls, x, *args):
        # if x is an integer or float
        if isinstance(x, Integer) or isinstance(x, Float):
            return round(x)

print(nint(x))
print(nint(1.5))
print(nint(1.4))
print(nint(2.5, 3))

expr = 1 + nint( 5 + a * (2 + 3))
print(expr)
print(expr.subs(a, 1.5))

