""" 6.8 ユークリッドの互除法 
p.247 リスト 6.12
p.248 リスト 6.13 """

def gcd(a, b):
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b

    return b

def gcd2(a, b):
    while b != 0:
        a, b = b, a % b

    return a


print(gcd(1274, 975))
print(gcd2(1274, 975))