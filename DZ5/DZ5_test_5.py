
def get_uniq_numbers(src: list):
    unique_num = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            unique_num.add(el)
        else:
            unique_num.discard(el)
        tmp.add(el)
    return unique_num


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))