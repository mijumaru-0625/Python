from math import e
from math import pi

# plotting.py を http://resources.codingthematrix.com/ からダウンロード
from plotting import plot 

print(F"e={e}")
print(F"π={pi}")

n = 20
print(F"n={n}")

w = e ** (2 * pi * 1j / n)
print(F"w = e ** (2πi)/n = {w}")

w_list = [w ** i for i in range(n)]
for i in range(n):
    print(F"i = {i} : w ** {i} = {w_list[i]}")

plot(w_list, 1.5) # 課題 1.4.8

print(F"e ** (iπ) + 1 = {e ** (pi * 1j) + 1}")