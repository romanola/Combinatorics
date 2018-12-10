#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 09.12.2018

INT_MIN = -32767
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
def cutRod(price, n):
    val = [0 for x in range(n + 1)]
    val[0] = 0
    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        max_val = INT_MIN
        for j in range(i):
            #print('___', max_val, (i, i-j-1),(price[j], val[i-j-1]))
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val
        #print(val[i])

    return val[n], val


@benchmark
def ExtendedBottomUpCutRod(p: list, n: int, price=0):
    """
    по заданным отрезку длине стержня и стоимости
    находит для каждой длины:
    максимальную прибыль
    и список раззрезов для заданной длины
    :param p: список стоимостей кусков стержня
    :param n: длина
    :param price: цена за разрез
    :return: список макс прибылей и список разрезов
    """
    res = [0] * (n + 1)
    seq = [[]] * (n + 1)
    for j in range(1, n + 1):
        q = 0
        cur_index = 0
        for i in range(j):
            if q < p[i] + res[j - i - 1] - price:
                q = p[i] + res[j - i - 1] - price
                cur_index = i
        seq[j] = seq[j - cur_index - 1] + [cur_index]
        res[j] = q
    return res, seq


if __name__ == '__main__':
    # test
    p = [1, 5, 8, 9, 10, 17, 17, 20]
    print(ExtendedBottomUpCutRod(p, len(p)))
    print("Maximum Obtainable Value is " + str(cutRod(p, len(p))))