from math import e
from math import pi

# plotting.py を http://resources.codingthematrix.com/ からダウンロード
from plotting import plot 
from image import file2image

def rotate(z: complex, t: float) -> complex:
    """ 複素数 z を t ラジアン回転させる関数 """
    return z * e ** (t * 1j)


S = { 2 + 2j, 3 + 2j, 
      1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

# 課題 1.4.18
plot({rotate(z, pi / 4.0) for z in S}, 4) # ブラウザ（Edge）が開いていないと正しく動作しない ?

data = file2image("img/img01.png")
width = len(data[0])
height = len(data)
print(width, height)
pts = {x + (height - y) * 1j for y, p_list in enumerate(data) for x, c in enumerate(p_list) if c[0]  < 120}

def center_to_o(z: complex) -> complex:
    """ 課題 1.4.11 S が表す画像の中心を原点にずらすような関数 """
    return z - width / 2.0 - height / 2.0 * 1j


# 課題 1.4.19
plot({rotate(z, pi / 4.0) for z in pts}, max(width, height) * 1.5)

# 課題 1.4.20
plot({rotate(center_to_o(z) * 0.5, pi / 4.0) for z in pts}, max(width, height))
