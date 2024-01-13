""" Python 機械学習プログラミング
3.3 ロジスティック回帰を使ってクラスの確率を予測するモデルの構築
p.57 -7 以上 7 未満の範囲にある値のシグモイド関数をプロットしてみよう """

import matplotlib.pyplot as plt
import numpy as np

# シグモイド関数を定義
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# 0.1 間隔で -7 以上　7 未満のデータを生成
z = np.arange(-7, 7, 0.1)
# 生成したデータでシグモイド関数を実行
phi_z = sigmoid(z)
# 元のデータとシグモイド関数の出力をプロット
plt.plot(z, phi_z)
# 垂直線を追加（z=0）
plt.axvline(0.0, color="k")
# y 軸の上限 / 下限を設定
plt.ylim(-0.1, 1.1)
# 軸のラベルを設定
plt.xlabel("z")
plt.ylabel("$\phi (z)$")
# y 軸の目盛を追加
plt.yticks([0.0, 0.5, 1.0])
# Axes クラスのオブジェクトの取得
ax = plt.gca()
# y 軸の目盛に合わせて水平グリッド線を追加
ax.yaxis.grid(True)
# グラフを表示
plt.tight_layout()
plt.show()

