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


def delta_target_population(population):
    """ 引数の人口を、ターゲットとの差を絶対値で返します """
    return abs(population - target_population)

current_index_list = []
current_delta = 0

def update_current(total_population, index_list:list):
    global current_index_list, current_delta
        
    current_index_list = copy.copy(index_list)
    current_delta = delta_target_population(total_population)

    pref_names = [pref_list[i] for i in index_list]
    print(pref_names, F"{total_population:,}", F"ターゲットとの差{current_delta:,}", )


update_current(0, current_index_list)


def search(total_population, index_list:list):
    delta = delta_target_population(total_population)

    if total_population > target_population and delta > current_delta:
        return

    if delta <= current_delta:
        update_current(total_population, index_list) # ベストデータの更新

    for j in range(index_list[-1] + 1, len(pref_list)):
        index_list.append(j) 
        search(total_population + population_data[pref_list[j]], index_list)
        index_list.pop()



for i in range(len(pref_list)):
    search(population_data[pref_list[i]], [i])                
            
print(F'{population_data["栃木県"]:,}')
print(F'{population_data["石川県"]:,}')
print(F'{population_data["静岡県"]:,}')
print(F'{population_data["愛媛県"]:,}')
print(F'{population_data["熊本県"]:,}')
p = population_data["栃木県"] + population_data["石川県"] + population_data["静岡県"] \
    + population_data["愛媛県"]+ population_data["熊本県"]
print(F'{p:,}')
