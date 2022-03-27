import csv
import sys
from sys import argv
from itertools import zip_longest


def main(*args):
    with open(argv[1], 'r', encoding='utf-8') as users, open(argv[2], 'r', encoding='utf-8') as hobby:
        s = []
        f = []

        for text1 in users:
            s.append(text1.strip())

        for text2 in hobby:
            f.append(text2)

        if len(s) < len(f):
            raise SystemExit(1)

    dict_out = dict(zip_longest(s, f, fillvalue=None))

    with open(argv[3], 'w', encoding='utf-8') as fw:
        for key, val in dict_out.items():
            fw.write('{}:{}\n'.format(key, val))


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
