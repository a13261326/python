#*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    generator = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
    return generator


n = 10
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))


