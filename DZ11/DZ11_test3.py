class Check_List(Exception):
    pass


def Data_List(*val):
    d = []
    prompt = "Введите данные: ('stop' для остановки)  :"
    active = True
    while active:
        val = input(prompt)
        if val == 'stop':
            break
        elif not val.isdigit():
            try:
                raise Check_List
            except Check_List:
                print(f" Ошибка ввода : {str(val)}")
        else:
            d.append(int(val))
    return d


if __name__ == '__main__':
    print(Data_List())
