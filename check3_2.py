import copy

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

# 目的の人口
target_population = 10000000

pref_list = list(population_data.keys())    

def count_population(index_list:list):
    """ 引数のリストで与えた都道府県の人口を計算します """
    pop = 0

    for i in index_list:
        pop += population_data[pref_list[i]]

    return pop


def delta_target_population(population):
    """ 引数の人口を、ターゲットとの差を絶対値で返します """
    return abs(population - target_population)

current_index_list = []
current_delta = 0

def update_current(index_list:list):
    global current_index_list, current_delta
        
    current_index_list = copy.copy(index_list)
    current_delta = delta_target_population(count_population(index_list))

    pref_names = [pref_list[i] for i in index_list]
    population = count_population(index_list)
    print(pref_names, F"{population:,}", F"ターゲットとの差{current_delta:,}", )


update_current(current_index_list)


def make_index_list(index_list:list):
    population = count_population(index_list)
    delta = delta_target_population(population)

    if population > target_population and delta > current_delta:
        return

    if delta <= current_delta:
        update_current(index_list) # ベストデータの更新

    
    for j in range(index_list[-1] + 1, len(pref_list)):
        index_list.append(j) 
        make_index_list(index_list)
        index_list.pop()


for i in range(len(pref_list)):
    make_index_list([i])                
            
            
