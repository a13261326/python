
cube_list = [i ** 3 for i in range(1000) if i % 2 != 0]
seven_list = []
seventeen_list = []
n7_sum = 0
n17_sum = 0
for num in cube_list:
    num_two = num + 17
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
        if sum % 7:
            seven_list.append(sum)
            n7_sum += sum
    while (num_two != 0):
        sum = sum + num_two % 10
        num_two = num_two // 10
        if sum % 7:
            seventeen_list.append(sum)
            n17_sum += sum
print(cube_list)
print(seven_list)
print(n7_sum)
print(seventeen_list)
print(n17_sum)
