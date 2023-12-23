from sympy import sieve

print([i for i in sieve.primerange(1, 200)]) # 素数を求める

from sympy import isprime

print(isprime(101)) # 素数の判定
