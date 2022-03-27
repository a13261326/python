def type_logger(calc_cube):
    result = []
    lst = []
    types = []
    a_dict = {}
    n = int(input("Введите количество элементов : "))
    for i in range(0, n):
        ele = int(input("Введите  элемент:"))
        lst.append(ele)
    for x in lst:
        types.append(type(x))
        result.append(calc_cube(x))
        a_dict = {key: value for key, value in zip(result, types)}
    return print(f'{calc_cube.__name__} {a_dict}')


@type_logger
def calc_cube(x):
    return x ** 3
