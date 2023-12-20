""" p.44 2.6 大規模な機械学習と確率的勾配降下法 """

import pandas as pd
import numpy as np
from numpy.random import seed

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
        self.const_ = []
        # 訓練回数分まで訓練データを反復
        for i in range(self.n_iter):
            pass


    def _shuffle(self, X, y):
        """ 訓練データをシャッフル """


    def _initialize_weights(self, m):
        """ 重みを小さな乱数に初期化 """
        self.rgen = np.random.RandomState(self.random_state)
        self.w_ = self.rgen.normal(loc=0.0, scale=0.01, size=1 + m)
        self.w_initialized = True



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

