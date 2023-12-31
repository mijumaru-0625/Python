"""
p.145 ハノイの塔
"""

def move_disk(src, dest):
    global g_move_count
    g_move_count += 1

    match src:
        case "a":
            disk = a_list.pop()
        case "b":
            disk = b_list.pop()
        case "c":
            disk = c_list.pop()

    match dest:
        case "a":
            a_list.append(disk)
        case "b":
            b_list.append(disk)
        case "c":
            c_list.append(disk)    


def disk_to_string():
    return F"a{a_list} b{b_list} c{c_list}"
    

def hanoi(n, src, dest, via):
    """
    n
        円盤の番号
    src
        移動元
    dest
        移動先
    via
        経由場所
    """
    if n > 1:
        hanoi(n - 1, src, via, dest)

        move_disk(src, dest)
        print(F"円盤{n}を、{src} -> {dest}、{disk_to_string()}")

        hanoi(n - 1, via, dest, src)
    else:
        move_disk(src, dest)
        print(F"円盤{n}を、{src} -> {dest}、{disk_to_string()}")


g_move_count = 0
n = int(input("円盤の枚数を入力\n"))

a_list = [i for i in range(n, 0, -1)]
b_list = []
c_list = []
print("最初の状態", disk_to_string())

hanoi(n, "a", "b", "c")

print("移動回数", g_move_count)