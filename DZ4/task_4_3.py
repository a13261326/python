from requests import get, utils
import re
import datetime
response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
y = (content.split("ID=")[0])
date_value = re.search(r'Date=">?([^" name=">]+)', y).group(1)


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""

    for i in content.split("ID="):
        if code.upper() in i:
            result_value = float(re.search(r'Name><Value>?([^</Value></Valute><Valute>]+)', i).group(1).replace(',', '.'))
            return result_value



print(currency_rates("huf"), date_value)
print(currency_rates("noname"))
