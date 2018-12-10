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


def ASP_iterative(s, f):
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
def get_subset(s, f, i, j):
    if i == 0:
        start = 0
    else:
        start = f[i - 1]
    if j == len(s):
        finish = 1 << 20
    else:
        finish = s[j]
    res = [(s[k], f[k]) for k in range(len(s)) if s[k] > start and f[k] < finish]
    return res



@benchmark
def ASP_Dynamic(s, f, v):
    """
    Динамический алгоритм
    :param s: список начал
    :param f: список концов
    :param v: список цен
    :return:
    """
    l = len(s)
    vals = [[None for _ in range(l)] for _ in range(l)]
    indxs = [[None for _ in range(l)] for _ in range(l)]
    for a in range(l):
        vals[a][a] = 0
    for c1 in range(1, len(vals)):
        for c2 in range(c1, len(vals)):
            i, j = c2 - c1, c2
            mx = 0
            kx = -1
            for k in range(i + 1, j):
                if get_subset(s, f, i, j):
                    tmp = vals[i][k] + vals[k][j] + v[k]
                    if tmp > mx:
                        mx = tmp
                        kx = k
            vals[i][j] = mx
            indxs[i][j] = kx
    return vals, indxs


def get_res1(indxs, i, j):

    if indxs[i][j] == -1 or indxs[i][j] is None:
        return ''
    else:
        k = indxs[i][j]
        return get_res1(indxs, i, k) + ' ' + str(k) + ' ' + get_res1(indxs, k, j)

def get_res2(vals, i, j):
    if vals[i][j] == 0 or vals[i][j] is None:
        return ''
    else:
        k = vals[i][j]
        return get_res1(vals, i, k) + ' ' + str(k) + ' ' + get_res1(vals, k, j)

# @benchmark
# def GreedyActivivtySelector(s, f):
    """
    жадный алгоритм
    :param s: список начал процессов
    :param f: список концов процессов
    :return: макс множество процессов
    """
    n = len(s)
    A = [(s[0], f[0])]
    k = 1
    for m in range(2, n):
        if s[m] >= f[k]:
            A += [(s[m], f[m])]
            k = m
    return A
@benchmark
def RecursiveActiveSelector(start, finish, k, n):
    """
    рекурсивный алгоритм
    :param start: список начал процессов
    :param finish: список конец процессов
    :param k: стартовое время
    :param n: конечное время
    :return: макс множество процессов
    """
    m = k + 1

    if k == 0:
        return [(start[m], finish[m])]+ RecursiveActiveSelector(start, finish, m, n)
    while m <= n and start[m] < finish[k]:
        m += 1
    if m <= n:
        return [(start[m], finish[m])] + RecursiveActiveSelector(start, finish, m, n)
    else:
        return []

if __name__ == '__main__':
    s = [0, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6]
    f = [2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8]
    v = [3, 4, 4, 4, 4, 2, 4, 4, 4, 4, 3]
    r1, r2 = ASP_Dynamic(s, f, v)
    print('Task 1')
    print("Dynamic", get_res1(r2, 0, len(s) - 1))
    print('Iterative', ASP_iterative(s, f))
    print('\nTask 2')
    r1, r2 = ASP_Dynamic(s, f, v)
    print("Dynamic", get_res2(r2, 0, len(s) - 1))
    # print(GreedyActivivtySelector(s, f))
    print('\nTask 3')
    # t_start = time.time()
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]
    print(RecursiveActiveSelector(s, f, 0, 5))
    # t_end = time.time()
    # print(t_end - t_start)
    print('Iterative', ASP_iterative(s, f))
