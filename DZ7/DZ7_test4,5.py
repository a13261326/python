import os
import pprint


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(f'Корневая директория нашего проекта - {BASE_DIR}')
tens = 0
hundreds = 0
thousands = 0
ten_thousands = 0
hund_thousands = 0
millions = 0
tens_ext = []
hundreds_ext = []
thousands_ext = []
ten_thousands_ext = []
hund_thousands_ext = []
hund_thousands_ext = []
millions_ext = []

for top, dirs, files in os.walk(BASE_DIR):
    file_size = 0
    for nm in files:
        file_ext = str(nm).split(".")[-1]
        # print(h)
        file_size = os.stat(os.path.join(top, nm)).st_size
        # print(os.path.join(top, nm))
        if file_size <= 100:
            tens = tens + 1
            if file_ext not in tens_ext:
                tens_ext.append(file_ext)
        elif file_size > 100 and file_size <= 1000:
            hundreds = hundreds + 1
            if file_ext not in hundreds_ext:
                hundreds_ext.append(file_ext)
        elif file_size > 1000 and file_size <= 10000:
            thousands = thousands + 1
            if file_ext not in thousands_ext:
                thousands_ext.append(file_ext)
        elif file_size > 10000 and file_size <= 100000:
            ten_thousands = ten_thousands + 1
            if file_ext not in ten_thousands_ext:
                ten_thousands_ext.append(file_ext)
        elif file_size > 100000 and file_size <= 1000000:
            hund_thousands = hund_thousands + 1
            if file_ext not in hund_thousands_ext:
                hund_thousands_ext.append(file_ext)
        elif file_size > 1000000:
            millions = millions + 1
            if file_ext not in millions_ext:
                millions_ext.append(file_ext)

objects = ['100', '1000', '10000', '10000', '100000']
categories = [(tens, tens_ext), (hundreds, hundreds_ext), (thousands, thousands_ext),(ten_thousands, ten_thousands_ext),(hund_thousands, hund_thousands_ext),(millions, millions_ext)]
a_dict = {key: value for key, value in zip(objects, categories)}
pprint.pprint(a_dict)

with open(f'{BASE_DIR}_summary.json', 'w', encoding='utf-8') as fw:
    for key,val in a_dict.items():
        fw.write('{}:{}\n'.format(key, val))