#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 01.12.2018
import time
def memo(f):
    """
    Декортор @memo для кешування функції f
    """
    m = {}

    def _memo(*args):
        if args in m:
            return m[args]
        else:
            res = f(*args)
            m[args] = res
            return res
    return _memo
@memo #запам'ятовуємо пораховані числа, щоб не рахувати знов при рекурсивному підході
def fibon(n):
    """
    Шукає n-те число Фібоначчі
    :param n: номер
    :return: шукане число
    """
    if n == 1 or n == 2:
        return 1
    return fibon(n - 1) + fibon(n - 2)


if __name__ == '__main__':
    n = 0
    while True:
        n += 1
        t_start = time.time()
        print('fibon({}) = {}'.format(n, fibon(n)))
        t_end = time.time()
        if t_end - t_start >= 60:
            print('\n---- n = {} ----\n'.format(n))
            break