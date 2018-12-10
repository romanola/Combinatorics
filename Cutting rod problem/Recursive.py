#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 09.12.2018

import sys
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


class MyList(list):
    """
    список со взятием хэша
    """
    def __hash__(self):
        return str.__hash__(str(self))


#@benchmark
def CutRodRecursively(p, n):
    if n == 0:
        return 0
    q = - sys.maxsize - 1
    for i in range(n):
        q = max(q, p[i] + CutRodRecursively(p, n - i - 1))
    return q


@memo
#@benchmark
def CutRodDynamic(p: MyList, n: int):
    if n == 0:
        return 0
    q = - sys.maxsize - 1
    for i in range(n):
        q = max(q, p[i] + CutRodDynamic(p, n - i - 1))  # разбиваем задачи на подзадачи (рекурсивно)
    return q


if __name__ == '__main__':
    # test
    p = MyList([1, 5, 8, 9, 10, 17, 17, 20, 24, 30])
    print(CutRodRecursively(p, len(p)))
    print(CutRodDynamic(p, len(p)))