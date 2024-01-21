def convert_to_Japanese_year(year):
    if year < 1869 or 2020 < year:
        print("引数は 1869 以上、2020 以下にしてください。")
        return
    
    wareki = {"明治": 1868,
              "大正": 1912,
              "昭和": 1926,
              "平成": 1989,
              "令和": 2019,
              "未定": 9999}   # 最後のデータはダミー

    before_nengo = ""
    before_gannnen = 0
    for nengo, gannnen in wareki.items():
        if year < gannnen:
            print(before_nengo, year - before_gannnen + 1, "年")
            return

        before_nengo = nengo
        before_gannnen = gannnen

convert_to_Japanese_year(1989)
convert_to_Japanese_year(2019)
convert_to_Japanese_year(2000)