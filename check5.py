input_data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]
print("input data :", input_data)

count_list = [0] * 10
print("count list :", count_list)

for i in input_data:
    count_list[i] += 1

print("count list :", count_list)

j = 0
for i in range(len(count_list)):
    for _ in range(count_list[i]):
        input_data[j] = i
        j += 1


print("sorted data:", input_data)