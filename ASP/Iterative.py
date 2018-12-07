#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 07.12.2018
import time

def benchmark(f):
    """
    Декоратор @benchmark для вычисления времени работы функции f
    """
    def _benchmark(*args, **kw):
        t = time.clock()
        rez = f(*args, **kw)
        t = time.clock() - t
        print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
        return rez
    return _benchmark


@benchmark
def ASPiterative(s, f):
    """
    итеративый алгоритм
    процессор задается кортежом (start time, finish time)
    :param s: список начал процессов
    :param f: список концов процессов
    :return: A - максимальное множество процессоров
    """
    A = []  # инициализируем множество
    n = len(f)
    i = 0
    A.append((s[i], f[i]))
    for j in range(n):
        if s[j] >= f[i]:
            A.append((s[j], f[j]))
            i = j
    return A


if __name__ == '__main__':
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    print(ASPiterative(s, f))