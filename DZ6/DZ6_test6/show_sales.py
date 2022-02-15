import math
import sys
from sys import argv


def main(*args):
    n = 0  # обнуляем счётчик
    length = format(len(*args))  # количество аргументов
    if  int(length) > 1 and not argv[1].replace('.', '', 1).isdigit():  # проверяем аргументы на число и количество
        print('Введите число,не более двух!!')
        raise SystemExit(1)
    if  int(length) > 2 and not argv[2].replace('.', '', 1).isdigit():
        print('Введите число, не более двух!')
        raise SystemExit(1)
    if  int(length) > 3 :
        print('Введите число, не более двух!')
        raise SystemExit(1)
    # знаю что так делать нельзя,дублирование идёт, но уже голова не соображает(((

    if length == '1':  # без аргументов
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for line in f:
                n += 1
                print(line)
    elif length == '2':  # 1 аргумент
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for line in f:
                n += 1
                if n >= int(argv[1]):
                    print(line)
    elif length == '3':  # 2 аргумента
        m = (min(int(argv[1]), int(argv[2])))
        l = (max(int(argv[1]), int(argv[2])))
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for line in f:
                n += 1
                if n >= m:
                    print(line)
                if n >= l:
                    exit()


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
