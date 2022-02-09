from requests import get, utils
import re


def currency_rates(code) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    # pprint(content.split("ID="))
    for i in content.split("ID="):
        if code.upper() in i:
            result_value = float(re.search(r'Name><Value>?([^</Value></Valute><Valute>]+)', i).group(1).replace(',', '.'))
            return result_value

