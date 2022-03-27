#Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
import sys


def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    for num in range(1, 10 ** 6 + 1, 2):
       yield num ** 2


n = 10
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration