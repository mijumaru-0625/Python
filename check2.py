""" 理解度 Check !
第2章 """

print("1950～2050年のうるう年")
for year in range(1950, 2051):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            pass
        else:
            print(year, end=" ")

# 答えに出力結果がなくてプログラムだったのでそのまま打ち込みます
# leap_year.py
            
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
        
    else:
        return False
    
print()
print("回答")
for i in range(1950, 2051):
    #print(str(i) + " " + str(is_leap_year(i)))
    if is_leap_year(i):
        print(str(i), end=" ")    
