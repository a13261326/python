class Check_List(Exception):
    pass

class Warehouse:
    Printers = {}
    Scanners = {}
    Xerox = {}

    def __init__(self, type, obj):
        for i in Printers, Scanners, Xerox:
            if type == i:
                self.type = obj
                print(self.type)
                break


class Hardware:
    def __init__(self, type_name, brand_name, item_name, price, total_amount):
        self.type_name = type_name
        self.brand_name = brand_name
        self.item_name = item_name
        self.price = price
        self.total_amount = total_amount
        self.items = {'Тип оргтехники': self.type_name, 'Производитель': self.brand_name, 'Цена: ': self.price,
                      'Количество': self.total_amount}
        if not self.total_amount.isdigit():
            try:
                raise Check_List
            except Check_List:
                print(f" Ошибка ввода : {str(total_amount)}")
                exit()

class Printers(Hardware):
    def __init__(self, print_rate, print_quality):
        self.print_rate = print_rate
        self.print_quality = print_quality
        self.item_attr = {'Скорость': self.print_rate, 'Качество': self.print_quality}


class Scanners(Hardware):
    def __init__(self, color_depth, scan_format):
        self.color_depth = color_depth
        self.scan_format = scan_format
        self.item_attr = {'Глубина цвета': self.color_depth, 'Формат': self.scan_format}
        # return self.Scanners_attr


class Xerox(Hardware):
    def __init__(self, weight, lenth):
        self.weight = weight
        self.lenth = lenth
        self.item_attr = {'Вес': self.weight, 'Длина': self.lenth}


h = Hardware('Принтер', 'Samsung', 'Samsung 1111', '1000', '2')
p = Printers('25 p/sec', '1080')
s = Scanners('300 dpi', 'A4,A3')
x = Xerox('20', '200')

h.items.update(p.item_attr)
Warehouse(Printers, h.items)
