
def my_filter(L: list, num: int) -> list:
    """ 入力 : 数のリスト L と正の整数 num
    出力 : L のうち num の倍数を含まない数のリスト
    例 : list = [1, 2, 4, 5, 7] 及び num = 2 を与えると [1, 5, 7] を返す。
    問題 1.7.1 """
    return [n for n in L if n % num != 0]

assert my_filter([1, 2, 4, 5, 7], 2) == [1, 5, 7]

def my_lists(L: list[int]) -> list[list[int]]:
    """ 入力 : 非負整数のリスト L
    出力 : L のそれぞれの要素 x を 1, 2, ..., x から成るリストにしたリスト 
    例1 : [1, 2, 4] を与えると [[1], [1, 2], [1, 2, 3, 4]] が返される。
    例2 : [0] を与えると [[]] が返される。
    問題 1.7.2 """
    # ret = []
    # for n in L:
    #     ret.append([i for i in range(1, n + 1)])

    # return ret
    return [[i for i in range(1, n + 1)] for n in L]    

assert my_lists([1, 2, 4]) == [[1], [1, 2], [1, 2, 3, 4]]
assert my_lists([0]) == [[]]

def my_function_composition(f: dict, g: dict) -> dict:
    """ 入力 : 辞書として定義された 2 つの関数 f 、g 。ただし、g・f が存在すること。
    出力 : g・f を表す辞書
    例 : f = {0: "a", 1: "b"} 、g = {"a": "apple", "b": "banana"} を与えると、
    {0: "apple", 1: "banana"} を返す。
    問題 1.7.3 """
    return {k:g[f[k]] for k, v in f.items()}

assert my_function_composition({0: "a", 1: "b"}, {"a": "apple", "b": "banana"}) == {0: "apple", 1: "banana"}