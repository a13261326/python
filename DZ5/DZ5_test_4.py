#Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например
#src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#result = [12, 44, 4, 10, 78, 123]



def get_numbers(src: list):
    result = []
    for a in range(1,len(src)):
        if src[a] > src[a - 1]:
            result.append(src[a])
    return result


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))



