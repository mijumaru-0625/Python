# plotting.py を http://resources.codingthematrix.com/ からダウンロード
from plotting import plot 
from image import file2image

# 課題 1.4.10

data = file2image("img/img01.png")
width = len(data[0])
height = len(data)
print(width, height)

pts = [x + (height - y) * 1j for y, p_list in enumerate(data) for x, c in enumerate(p_list) if c[0]  < 120] 
plot(pts, max(width, height))

def f(z: complex):
    """ 課題 1.4.11 S が表す画像の中心を原点にずらすような関数 """
    return z - width / 2.0 - height / 2.0 * 1j

plot([f(z) for z in pts], max(width, height))

# 課題 1.4.12
plot([z * 1j * 0.5 for z in pts], max(width, height))