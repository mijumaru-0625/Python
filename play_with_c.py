
src = "10101 00100 10101 01011 11001 00011 01011 10101 00100 11001 11010"
print("暗号の文字", src)
tokens = str.split(src)

bits = ["0", "1"]
pass_key = ["".join((a, b, c, d, e)) for a in bits for b in bits for c in bits for d in bits for e in bits]
pass_key_value = [int(v, 2) for v in pass_key]
print("復号キーのリスト", pass_key)
#print(pass_key_value)

pass_key_to_int = {k:v for k, v in zip(pass_key, pass_key_value)}
#print(pass_key_to_int)

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?????"
int_to_chars = {i: v for i, v in enumerate(chars)}
print("数値 → 文字の対応表", int_to_chars)

print("暗号のリスト", tokens)
#print([pass_key_to_int[s] for s in tokens])
print("".join([int_to_chars[pass_key_to_int[s]] for s in tokens]))
print()

def f(c_str: str, k_str: str) -> str:
    """ 暗号 c_str に復号キー k_str を XOR します """
    ret = []
    for c, k in zip(list(c_str), list(k_str)):
        if c == k:
            ret.append("0")
        else:
            ret.append("1")

    return "".join(ret)


for k in pass_key:
    print("復号キー", k)
    answer = [f(s, k) for s in tokens]
    print(answer)
    print("".join([int_to_chars[pass_key_to_int[s]] for s in answer]))
    print()

# 復号キー 10001 復号文字 EVE IS EVIL