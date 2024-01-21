""" 第6章 理解度 Check ! 問題1 """

input_data = "000000111111100111000000001111"

input_list = list(input_data)
output_data = []

search_char = "0"
output_counter = 0

for c in input_data:
    if c == search_char:
        output_counter += 1
    else:
        output_data.append(output_counter)
        output_counter = 1
        if search_char == "0":
            search_char = "1"
        else:
            search_char = "0"
else:
    output_data.append(output_counter)


print(output_data)