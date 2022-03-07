class ZeroValException(Exception):
    pass


def Zero_Div(val1, val2):
    try:
        if val2 == 0:
            raise ZeroValException(f" Ошибка: деление на 0: {str(val1)} / {str(val2)}")
        print(round(val1 / val2, 2))
    except ZeroValException as e:
        print(e)


if __name__ == '__main__':
    Zero_Div(23, 0)
