
def mySum(L: list):
    """ 入力 : 数のリスト
    出力 : そのリスト内の数の総和"""
    current = 0
    for x in L:
        current = current + x

    return current


def myProduct(L: list):
    """ 入力 : 数のリスト
    出力 : そのリスト内の数の総乗 """
    current = 1
    for x in L:
        current = current * x

    return current


def myMin(L: list):
    """ 入力 : 数のリスト
    出力 : そのリスト内の数の最小値 """
    current = 1.7976931348623157e+308
    for x in L:
        current = x if x < current else current

    return current


def myConcat(L: list[str]) -> str:
    """ 入力 : 文字列のリスト
    出力 : L 内の全ての文字列を連結してできた文字列 """
    current = ""
    for x in L:
        current = current + x

    return current


def myUnion(L: list(set)) -> set:
    """ 入力 : 集合のリスト
    出力 : L 内のすべての集合の和集合 """
    current = set()
    for x in L:
        current = current | x

    return current

