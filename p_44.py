""" p.44 2.6 大規模な機械学習と確率的勾配降下法 """

import pandas as pd
import numpy as np
from numpy.random import seed
import matplotlib.pyplot as plt

from p_28 import plot_decision_regions

class AdalineSDG(object):
    """ ADAptive LInear NEuron 分類器
    
    パラメータ
    ---------
    eta : float
        学習率（0.0 より大きく 1.0 以下の値）
    n_iter : int
        訓練データの訓練回数
    shuffle : bool （デフォルト: True）
        True の場合は、循環を回避するためにエポックごとに訓練データをシャッフル
    random_state : int
        重みを初期化するための乱数シード
        
    属性
    ----
    w_ : 1 次元配列
        適合後重み
    cost_ : リスト
        各エポックですべての訓練データの平均を求める誤差平方和コスト関数
    """
    def __init__(self, eta=0.01, n_iter=10, shuffle=True, random_state=None) -> None:
        # 学習率の初期化
        self.eta = eta
        # 訓練回数の初期化
        self.n_iter = n_iter
        # 重みの初期化フラグは False に設定
        self.w_initialized = False
        # 各エポックで訓練データをシャッフルするかどうかのフラグを初期化
        self.shuffle = shuffle
        # 乱数シードを設定
        self.random_state = random_state

    
    def fit(self, X, y):
        """ 訓練データに適合させる
        
        パラメータ
        ---------
        X : { 配列のようなデータ構造 }, shape = [n_examples, n_features]
            訓練データ
            n_examples は訓練データの個数、n_features は特徴量の個数
        y : 配列のようなデータ構造、shape = [n_examples]
            目的変数
            
        戻り値
        -----
        self : object
        """
        # 重みベクトルの生成
        self._initialize_weights(X.shape[1])
        # コストを格納するリストの生成
        self.cost_ = []
        # 訓練回数分まで訓練データを反復
        for i in range(self.n_iter):
            # 指定された場合は訓練データをシャッフル
            if self.shuffle:
                X, y = self._shuffle(X, y)
            # 各訓練データのコストを格納するリストの生成
            cost = []
            # 各訓練データに対する計算
            for xi, target in zip(X, y):
                # 特徴量 xi と目的変数 y を用いた重みの更新とコストの計算
                cost.append(self._update_weights(xi, target))
            # 訓練データの平均コストの計算
            avg_cost = sum(cost) / len(y)
            # 平均コストを格納
            self.cost_.append(avg_cost)

        return self
    
    def partial_fit(self, X, y):
        """ 重みを再初期化することなく訓練データに適合させる """
        # 初期化されていない場合は初期化を実行
        if not self.w_initialized:
            self._initialize_weights(X.shape[1])
        # 目的変数 y の要素数が 2 以上の場合は各訓練データの特徴量 xi と目的変数 target で重みを更新
        if y.ravel().shape[0] > 1:
            for xi, target in zip(X, y):
                self._update_weights(xi, target)
        # 目的変数 y の要素数が 1 の場合は訓練データ全体の特徴量 X と目的変数 y で重みを更新
        else:
            self._update_weights(X, y)

        return self

    def _shuffle(self, X, y):
        """ 訓練データをシャッフル """
        r = self.rgen.permutation(len(y))
        return X[r], y[r]

    def _initialize_weights(self, m):
        """ 重みを小さな乱数に初期化 """
        self.rgen = np.random.RandomState(self.random_state)
        self.w_ = self.rgen.normal(loc=0.0, scale=0.01, size=1 + m)
        self.w_initialized = True

    def _update_weights(self, xi, target):
        """ ADALINE の学習規則を用いて重みを更新 """
        # 活性化関数の出力の計算
        output = self.activation(self.net_input(xi)) # 1 個のデータで複数のデータでも同じように扱えるのではないか?
        # 誤差の計算
        error = (target - output)
        # 重み w1, ..., wm の更新
        self.w_[1:] += self.eta * xi.dot(error)
        # 重み w0 の更新
        self.w_[0] += self.eta * error
        # コストの計算
        cost = 0.5 * error ** 2
        return cost
        
    def net_input(self, X):
        """ 総入力を計算 """
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        """ 線形活性化関数の出力を計算 """
        return X
    
    def predict(self, X):
        """ 1 ステップ後のクラスラベルを返す """
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)


# 入力データの準備
df = pd.read_csv("iris.data", header=None, encoding="utf-8")
y = df.iloc[0:100, 4].values
y = np.where(y == "Iris-setosa", -1, 1)
X = df.iloc[0:100, [0, 2]].values

# データのコピー
X_std = np.copy(X)
# 各列の標準化
X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

# 確率的勾配降下法による ADALINE の学習
ada_sdg = AdalineSDG(n_iter=15, eta=0.01, random_state=1)
# モデルへの適合
ada_sdg.fit(X_std, y)
# 境界領域のプロット
plot_decision_regions(X_std, y, classifier=ada_sdg)
# タイトルの設定
plt.title("Adaline - Stochastic Gradient Descent")
# 軸のラベル
plt.xlabel("sepal length [standardized]")
plt.ylabel("petal length [standardized]")
# 凡例の設定（左上に配置）
plt.legend(loc="upper left")
plt.tight_layout()
# プロットの表示
plt.show()

# エポックとコストの折れ線グラフのプロット
plt.plot(range(1, len(ada_sdg.cost_) + 1), ada_sdg.cost_, marker="o")
# 軸のラベルの設定
plt.xlabel("Epochs")
plt.ylabel("Average Cost")
# プロットの表示
plt.tight_layout()
plt.show()
