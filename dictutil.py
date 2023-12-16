def cubes(L: list) -> list:
    """ 入力 : 数のリスト L
    出力 :  i 番目の要素が L の i 番目の要素の 3 乗になっている数のリスト 
    例 : 入力 [1, 2, 3] 、出力 [1, 8, 27]
     p.38 課題 0.5.29 """
    return [x ** 3 for x in L]


def dict2list(dct: dict, keylist: list) -> list:
    """ 入力 : 辞書 dct 、dct のキーからなるリスト keylist
    出力 : i = 0, 1, 2, ... , len(keylist) - 1 に対して L[i] = dct[keylist[i]] となるようなリスト L
    例 : 入力 dct = {"a": "A", "b": "B", "c": "C"} と keylist = ["b", "c", "a"] 、
         出力 ["B", "C", "A"]
    p.38 課題 0.5.30 """
    return [dct[k] for k in keylist]


def list2dict(L: list, keylist: list) -> dict:
    """ 入力 : リスト L 、変更不可能な要素からなるリスト keylist
    出力 : i = 0, 1, 2, ..., len(L) - 1 に対して、keylist[i] を L[i] に写像する辞書
    例 : 入力 L = ["A", "B", "C"] と keylist = ["a", "b", "c"] 、
         出力 {"a": "A", "b": "B", "c": "C"}
    p.38 課題 0.5.31 """
    return {k: v for k, v in zip(keylist, L)}


def all_3_digit_numbers(base: int, digits: set[int]) -> set:
    """ 入力 : 正の整数 base と、{0, 1, 2, ..., base - 1} である集合 digits
    出力 : 底が base である 3 つの数字全てから成る数の集合

    p.38 課題 0.5.32 """
    return set([x1 * base ** 2 + x2 * base * 1 + x3 for x1 in digits for x2 in digits for x3 in digits])


if __name__ == "__main__":
    assert cubes([1, 2, 3]) == [1, 8, 27]
    assert dict2list({"a": "A", "b": "B", "c": "C"}, ["b", "c", "a"]) == ["B", "C", "A"]
    assert list2dict(["A", "B", "C"], ["a", "b", "c"]) == {"a": "A", "b": "B", "c": "C"}
    assert all_3_digit_numbers(2, {0, 1}) == {0, 1, 2, 3, 4, 5, 6, 7}
    assert all_3_digit_numbers(3, {0, 1, 2}) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                 20, 21, 22, 23, 24, 25, 26}
