def solve1(a, b, c):
    """ ax + b = c を解く関数 """
    return (c - b) / a

# 10x + 5 = 30 を解く
print(solve1(10, 5, 30))

# (10 + 5i)x + 5 = 20 を解く
print(solve1(10 + 5j, 5, 20))

# plotting.py を http://resources.codingthematrix.com/ からダウンロード
from plotting import plot 

S = { 2 + 2j, 3 + 2j, 
      1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
plot(S, 4) # ブラウザ（Edge）が開いていないと正しく動作しない

plot({1 + 2j + z for z in S}, 4)
plot({-2 - 2j + z for z in S}, 4)