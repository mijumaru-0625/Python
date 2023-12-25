"""
第3章 3.2 scikit-learn 活用へのファーストステップ：パーセプトロンの訓練
"""

from sklearn import datasets
import numpy as np 
# Iris データセットをロード
iris = datasets.load_iris()
# 3、4 列目の特徴量を抽出
X = iris.data[:, [2, 3]]
# クラスラベルを取得
y = iris.target
# 一意なクラスラベルを出力
print("Class labels:", np.unique(y))

from sklearn.model_selection import train_test_split
# 訓練データとテストデータに分割
# 全体の 30 % をテストデータにする
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

print("Labels counts in y:", np.bincount(y))
print("Labels counts in y_train:", np.bincount(y_train))
print("Labels counts in y_test:", np.bincount(y_test))

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# 訓練データの平均と標準偏差を計算
sc.fit(X_train)
# 平均と標準偏差を用いて標準化
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

from sklearn.linear_model import Perceptron
# エポック数 40、学習率 0.1 でパーセプトロンのインスタンスを生成
ppn = Perceptron(eta0=0.1, random_state=1)
# 訓練データをモデルに適合させる
ppn.fit(X_train_std, y_train)

# テストデータで予測を実施
y_pred = ppn.predict(X_test_std)
# 誤分類のデータ点の個数を表示
print("Misclassified examples: %d" % (y_test != y_pred).sum())

from sklearn.metrics import accuracy_score
# 分類の正解率を表示
print("Accuracy: %.3f" % accuracy_score(y_test, y_pred))

print("Accuracy(score): %.3f" % ppn.score(X_test_std, y_test))

from p_28 import plot_decision_regions
import matplotlib.pyplot as plt

# 訓練データとテストデータの特徴量を行方向に結合
X_combined_std = np.vstack((X_train_std, X_test_std))
# 訓練データとテストデータのクラスラベルを結合
y_combined = np.hstack((y_train, y_test))
# 決定境界のプロット
plot_decision_regions(X=X_combined_std, y=y_combined, classifier=ppn, test_idx=range(105, 150))
# 軸ラベルの設定
plt.xlabel("petal length [standardized]")
plt.ylabel("petal width [standardized]")
# 凡例の配置（左上に配置）
plt.legend(loc="upper left")
# グラフを表示
plt.tight_layout()
plt.show()

