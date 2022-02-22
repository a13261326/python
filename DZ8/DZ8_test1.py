import re


def email_parse(email: str) -> dict:
    #  """
    # Парсит переданную email-строку на атрибуты и возвращает словарь
    # :param email: строковое входное значение обрабатываемого email
    # :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    # """
    RE_MAIL = re.compile(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$')

    pass  # пишите реализацию здесь

    if RE_MAIL.match(email) is None:  # any found?
        raise ValueError(f'You entered wrong email:{email}')
    else:
        return print(dict(zip(('username', 'domain'), re.split(r'[.@\ ]', email, maxsplit=2))))

if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
