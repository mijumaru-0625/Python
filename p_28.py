import pandas as pd # pip install pandas
import matplotlib.pyplot as plt # pip install matplotlib
from matplotlib.colors import ListedColormap
import numpy as np

# https://archive.ics.uci.edu/dataset/53/iris
# のダウンロードボタンから iris.zip をダウンロード
# 解凍して iris.data を取得

def plot_input_data():
    """ p.28～30 入力データを散布図で確認する関数 """
    # 品種 setosa のプロット（赤の〇）
    plt.scatter(X[:50, 0], X[:50, 1], color="red", marker="o", label="setosa")
    # 品種 versicolor のプロット（青の×）
    plt.scatter(X[50:100, 0], X[50:100, 1], color="blue", marker="x", label="versicolor")
    # 軸ラベルの設定
    plt.xlabel("sepal length [cm]")
    plt.ylabel("petal length [cm]")
    # 凡例の設定（左上に配置）
    plt.legend(loc="upper left")
    # 図の表示
    plt.show()

class Perceptron(object):
    """ パーセプトロンの分類器 p.24 より

    パラメータ
    ------------------------
    eta : float
        学習率（0.0 よりおおきく 1.0 以下の値）
    n_iter : int
        訓練データの訓練回数
    random_state : int
        重みを初期化するための乱数シード

    属性
    ------------------------
    w_ : 1 次元配列
        適用後の重み
    errors_ : リスト
        各エポックでの誤分類（更新）の数
    """
    def __init__(self, eta=0.01, n_iter=50, random_state=1) -> None:
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state


    def fit(self, X, y):
        """ 訓練データに適合させる

        パラメータ
        ------------------------
        X : { 配列のようなデータ構造 }, shape = [n_examples, n_features]
            訓練データ
            n_exsamples は訓練データの個数、n_features は特徴量の個数
        y : 配列のようなデータ構造, shape = [n_examples]
            目的変数

        戻り値
        ------------------------
        self : object 
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter): # 訓練回数分まで訓練データを反復
            errors = 0
            for xi, target in zip(X, y): # 各訓練データで重みを更新
                # 重み w1, ..., wm の更新
                # Δwj = η(yi - y^i)xj i (j=1, ..., m)
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                # 重み w0 の更新 w0 = η(yi - y^i)
                self.w_[0] += update
                # 重みの更新が 0 でない場合は誤分類としてカウント
                errors += int(update != 0.0)

            #　反復毎の誤差を格納
            self.errors_.append(errors)

        return self
    

    def net_input(self, X):
        """ 総入力を計算 """
        return np.dot(X, self.w_[1:]) + self.w_[0] # np.dot は内積


    def predict(self, X):
        """ 1 ステップ後のクラスラベルを返す """
        return np.where(self.net_input(X) >= 0.0, 1, -1)


def plot_epochs_vs_number_of_updates():
    ''' 横軸をエポック数（≒検討回数）、縦軸を誤分類の個数とするグラフの表示 '''
    # エポックと誤分類の関係を表す折れ線グラフをプロット
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker="o")
    # 軸のラベルの設定
    plt.xlabel("Epochs")
    plt.ylabel("Number of update")
    # 図の表示
    plt.show()


def plot_decision_regions(X, y, classifier, resolution=0.02):
    # マーカーとカラーマップの準備
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # 決定領域のプロット
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    # グリッドポイントの生成
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    # 各特徴量を 1 次元配列に変換して予測を実行
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    # 予測結果をもとのグリッドポイントのデータサイズに変換
    Z = Z.reshape(xx1.shape)
    # グリッドポイントの等高線のプロット
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    # 軸の範囲の設定
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # クラスごとに訓練データをプロット
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0],
                    y=X[y == cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    marker=markers[idx],
                    label=cl,
                    edgecolors="black")
        

def plot_result():
    # 決定領域のプロット    
    plot_decision_regions(X, y, classifier=ppn)
    # 軸のラベルの設定
    plt.xlabel("sepal length [cm]")
    plt.ylabel("petal length [cm]")
    # 凡例の決定（左上に配置）
    plt.legend(loc="upper left")
    # 図の表示
    plt.show()


if __name__ == "__main__":
    # p.28

    df = pd.read_csv("iris.data", header=None, encoding="utf-8")
    print(df.tail())

    # p.29

    # 1-100 行目の目的変数の抽出、4 というのは 5 列目
    y = df.iloc[0:100, 4].values
    # Iris-setosa を -1、Iris-versicolor を 1 に変換
    y = np.where(y == "Iris-setosa", -1, 1)
    # 1-100 行目の 1、3 列目の抽出
    X = df.iloc[0:100, [0, 2]].values

    print("入力データの確認")
    plot_input_data() # 入力データの散布図を表示

    # p.30
    # パーセプトロンのオブジェクトの生成（インスタンス化）
    ppn = Perceptron(eta=0.1, n_iter=10)
    # 訓練データへのモデルモデルの適合
    ppn.fit(X, y)

    print("学習経過の確認")
    plot_epochs_vs_number_of_updates()

    print("決定領域のプロット")
    plot_result()
