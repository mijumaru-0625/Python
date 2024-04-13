l = list(range(10))
print(l)

# for ループ内でリストの remove はおかしくなることを確認した
for i in l:
    if i % 2 == 0:
        l.remove(i)
#l = [i for i in l if i % 2 == 0]
print(l)