import numpy as np
import pandas as pd # pip install pandas
import matplotlib.pyplot as plt

class AdalineGD(object):
    """ ADAptive LIner NEuron 分類器 p.36
    
    パラメータ
    ---------
    eta : float
        学習率（0.0 より大きく 1.0 以下の値）
    n_iter : int
        訓練データの訓練回数
    random_state : int
        重みを初期化するための乱数シード

    属性
    ----
    w_ : 1 次元配列
        適合後重み
    cost_ : リスト
        各エポックでの誤差平方和のコスト関数
    """
    def __init__(self, eta=0.01, n_iter=50, random_state=1) -> None:
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state


    def fit(self, X, y):
        """ 訓練データに適合させる
        
        パラメータ
        ---------
        X : { 配列のようなデータ構造 }, shape = [n_examples, n_features]
            訓練データ
            n_exsamples は訓練データの個数、n_features は特徴量の個数
        y : 配列のようなデータ構造, shape = [n_examples]
            目的変数

        戻り値
        -----
        self : object 
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter): # 訓練回数分まで訓練データを反復
            net_input = self.net_input(X) # データ数分の配列です

            # activation メソッドは単なる恒等関数（y=x の関数ということ）であるため、
            # このコードでは何の効果もないことに注意。代わりに、
            # 直接 `output = self.net_input(X)` と記述することもできた。
            # activation メソッドの目的は、より概念的なものである。
            # つまり、（後ほど説明する）ロジスティック回帰の場合は、
            # ロジスティック回帰の分類器を実装するためにシグモイド関数に変更することもできる
            output = self.activation(net_input)
            # 誤差 y(i) - Φ(z(i)) の計算
            errors = (y - output) # データ数分の配列です
            # w1, ..., wm の更新
            # Δwj = ηΣi(y(i)-Φ(z(i))xj(i)  (j=1, ..., m)
            self.w_[1:] += self.eta * X.T.dot(errors)
            # w0 の更新 Δw0 = ηΣi(y(i)-Φ(z(i))
            self.w_[0] += self.eta * errors.sum()
            # コスト関数の計算 J(w) = 1/2 Σi(y(i)-Φ(z(i))^2
            cost = (errors ** 2).sum() / 2.0
            # コストの格納
            self.cost_.append(cost)

        return self


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

# 描画領域を 1 行 2 列に分割
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# 勾配降下法による ADALINE の学習（学習率 eta=0.01）
ada1 = AdalineGD(n_iter=10, eta=0.01).fit(X, y)
# エポック数とコストの関係を表す折れ線グラフのプロット（縦軸のコストは常用対数）
ax[0].plot(range(1, len(ada1.cost_)+1), np.log10(ada1.cost_), marker="o")
# 軸ラベルの設定
ax[0].set_xlabel("Epoches")
ax[0].set_ylabel("log(Sum-squared-error)")
# タイトルの設定
ax[0].set_title("Adaline - Learning rate 0.01")

# 勾配降下法による ADALINE の学習（学習率 eta=0.0001）
ada2 = AdalineGD(n_iter=10, eta=0.0001).fit(X, y)
# エポック数とコストの関係を表す折れ線グラフのプロット
ax[1].plot(range(1, len(ada2.cost_)+1), ada2.cost_, marker="o")
# 軸ラベルの設定
ax[1].set_xlabel("Epoches")
ax[1].set_ylabel("Sum-squared-error")
# タイトルの設定
ax[1].set_title("Adaline - Learning rate 0.0001")

# 図の表示
plt.show()