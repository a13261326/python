# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

import re


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:

    for row in f:
        inf = ()
        list= []
        ip = (re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", row))
        ports = re.findall('1"(.*?)"-"', row)
        downloads = re.findall('T /(.*?)HT', row)
        daytime = re.findall('\[(.*?)\]', row)
        parsed_raw = (str(ip).strip('[]'), str(daytime).strip('[]'), str(downloads).strip('[]'), str(ports).strip('[]'))
        convertList = ', '.join([str(e) for e in parsed_raw])  # List comprehension
        print(convertList)

