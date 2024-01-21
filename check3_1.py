""" n 階に到達する組み合わせ(an)は、
2 階に到達する組み合わせ数(a2)
+ 3 階に到達する組み合わせ数(a3)
+ ... 
+ n - 1 階に到達する方法(an-1)
+ 1 階から直接 n 階に到達する 1 通り(これはa1)

an = a2 + a3 + ... + an-1 + 1 = a1 + a2 + a3 + ... + an-1

a1 = 1
a2 = a1 = 1
a3 = a1 + a2 = 1 + 1 = 2
a4 = a1 + a2 + a3 = 1 + 1 + 2 = 4
a5 = a1 + a2 + a3 + a4 = 1 + 1 + 2 + 4 = 8 """

def elevator_pattern(floor_number):
    if floor_number <= 1:
        return 1
    
    a = [0 for _ in range(floor_number + 1)]
    a[1] = 1

    for i in range(2, floor_number + 1):
        a[i] = sum(a)

    return a[floor_number] 


print(elevator_pattern(5))
print(elevator_pattern(10))
