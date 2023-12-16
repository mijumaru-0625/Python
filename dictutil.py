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
    return {x1 * base ** 2 + x2 * base * 1 + x3 for x1 in digits for x2 in digits for x3 in digits}


def listrange2dict(L: list) -> dict:
    """ 入力 : リスト L
    出力 : i = 0, 1, 2, ..., len(L) - 1 に対して、i を L[i] に写像する辞書
    p.41 課題 0.6.4 """
    return {k: v for k, v in enumerate(L)}


def makeInverseIndex(strlist: list[str]) -> dict[str, set[int]]:
    """ 文字列（文書）（←文字列のリストのこと）が与えられると、
    単語がその単語が現れる文書番号（←文字列のリストのインデックスのこと）から成る集合に
    写像する辞書（逆インデックス）を返す関数
    p.44 課題 0.6.6 """
    ret: dict[str, set[int]]= {}
    for index, line in enumerate(strlist):
        for token in  line.split():
            ret.setdefault(token, set())
            ret[token].add(index)
    
    return ret
            

def orSearch(inverseIndex: dict[str, set[int]], query: list[str]) -> set[int]:
    """ 逆インデックス inverseIndex と単語のリスト query を受け取り、
    query 内の単語のどれかが含まれている文書の文書番号の集合を返す関数
    p.44 課題 0.6.7 """
    ret: set[int] = set()
    for token in query:
        if token in inverseIndex:
            ret = ret | inverseIndex[token]

    return ret


def andSearch(inverseIndex: dict[str, set[int]], query: list[str]) -> set[int]:
    """ 逆インデックス inverseIndex と単語のリスト query を受け取り、
    query 内の単語の全てが含まれている文書の文書番号の集合を返す関数
    p.44 課題 0.6.8 """
    ret: set[int] = set()
    for v in inverseIndex.values(): # 行数の全体の集合を作る
        ret = ret | v

    for token in query:
        if token in inverseIndex:
            ret = ret & inverseIndex[token]
        else:
            ret = ret & set()

    return ret


def mini_search_engine():
    """ ミニ検索エンジン p.43 0.6.7"""
    with open("stories_small.txt") as f:
        lines_list = f.readlines()

    print(orSearch(makeInverseIndex(lines_list), ["for", "example"]))        
    print(andSearch(makeInverseIndex(lines_list), ["for", "example"]))        

    with open("stories_big.txt") as f:
        lines_list = f.readlines()

    print(orSearch(makeInverseIndex(lines_list), ["for", "example"]))        
    print(andSearch(makeInverseIndex(lines_list), ["for", "example"]))        


if __name__ == "__main__":
    mini_search_engine()
