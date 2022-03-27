class MyClass:

    @staticmethod
    def validate(s):
        y = s.split('-')
        if not y[0].isdigit() or int(y[0]) > 31 or int(y[0]) <= 0:
            return False
        elif not y[1].isdigit() or 0 <= int(y[1]) > 12 or int(y[1]) <= 0:
            return False
        elif not y[2].isdigit() or 0 <= int(y[2]) <= 0 or int(y[2]) <= 0:
            return False
        else:
            return True

    @classmethod
    def my_method(cls, param):  # Метод класса
        try:
            if MyClass.validate(param) is False:
                raise TypeError
            d = []
            for i in param.split('-'):
                d.append(int(i))
            print(f"{d[0]}\n{d[1]}\n{d[2]}\n")
        except TypeError:
            print(f"Некорректная дата")


if __name__ == '__main__':
    # print(MyClass.my_method(input(f'Введите дату в формате день-месяц-год: ')))
    MyClass.my_method('12-12-3002')
