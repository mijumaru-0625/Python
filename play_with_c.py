# plotting.py を http://resources.codingthematrix.com/ からダウンロード
from plotting import plot 

S = { 2 + 2j, 3 + 2j, 
      1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
plot(S, 4) # ブラウザ（Edge）が開いていないと正しく動作しない

plot({z / 2 for z in S}, 4)
#plot({-1 * z for z in S}, 4)
#plot({1j * z for z in S}, 4)

# 課題 1.4.8
plot({z * 1j * 0.5 for z in S}, 4)

# 課題 1.4.9
plot({z * 1j * 0.5 + 2 - 1j for z in S}, 4)
