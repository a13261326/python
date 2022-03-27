from pprint import pprint


def get_parse_attrs(text: str) -> tuple:
    # """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    r = text.split("-", 2)
    u = text.split()
    ip_addr = r[0]
    prod_type = u[6]
    req_time = r[2].split("]", 2)[0].replace('[', '')
    list = (ip_addr, req_time, prod_type)  # Ваша реализация здесь
    return list  # верните кортеж значений <remote_addr>, <request_time>, <request_type>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    # pass  # передавайте данные в функцию и наполняйте список list_out кортежами
    for text in fr:
        result = get_parse_attrs(text)
        list_out.append(result)
    pprint(list_out)
