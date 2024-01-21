# データ読み込み
with open("001_00.csv") as f:
    lines = f.readlines()

population_data = {}
for s in lines:
    tokens = s.split(",")
    for i in range(len(tokens)):
        token = tokens[i].strip('"')
        if token == "東京都" or  token == "北海道" or token.endswith("府") or token.endswith("県"):
            population_data[token] = int(tokens[i + 1])
            break 

# 読み込みデータの表示
print(len(population_data), population_data)

# 以降、[第4章] 理解度 Check ! 【問題2】回答

# 近づける値
goal = 10000000

# 各都道府県の人口、これは回答を利用しない
pref = list(population_data.values())

min_total = 0
def search(total, pos):
    global min_total
    if pos >= len(pref):
        return
    if total < goal:
        if abs(goal - (total + pref[pos])) < abs(goal - min_total):
            min_total = total + pref[pos]
        search(total + pref[pos], pos + 1)
        search(total, pos + 1)

search(0, 0)
print(min_total)