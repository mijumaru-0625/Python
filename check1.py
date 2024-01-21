""" 理解度 Check !
第1章 """

# 問題1
x = 3
def calc(x):
    x += 4
    return x

print(x) # 3 と表示
print(calc(x)) # 7 と表示
print(x) # 3 と表示

# 問題2
a = [3]
def calc(a):
    a[0] += 4
    return a

print(a) # [3] と表示
print(calc(a)) # [7] と表示
print(a) # [7] と表示

# 問題3
a = [3]
def calc(a):
    a = [4]
    return a

print(a) # [3] と表示
print(calc(a)) # [4] と表示
print(a) # [3] と表示