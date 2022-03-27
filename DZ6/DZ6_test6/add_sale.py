import csv
import sys
from sys import argv


def main(*args):
    length = format(len(*args))

    with open('bakery.csv', 'a', encoding='utf-8') as f:
        if argv[1].replace('.', '', 1).isdigit() and int(length) <= 2:
            print(argv[1], file=f)
        else:
            print('Введите  одно число!', type(argv[1]))
        raise SystemExit(1)




if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
