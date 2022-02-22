def val_checker(type=int):
    def check_accepts(f):
        def wrapper(x):
            if (isinstance(x, int)) and x > 0:
                return f(x)
            else:
                msg = f'wrong val {x}'
                raise ValueError(msg)

        return wrapper

    return check_accepts


@val_checker(int)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))