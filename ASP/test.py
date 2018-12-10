#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 09.12.2018

from time import time
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


def recursive(s, f, v, i, j):
    if not get_subset(s, f, i, j):
        return 0
    else:
        vals = [recursive(s, f, v, i, k) + recursive(s, f, v, k, j) + v[k] for k in range(i + 1, j)]
        return max(vals)

def big(s, f, k, n):
    for i in range(k + 1, n):
        if s[i] >= f[k]:
            return [(s[i], f[i])] + big(s, f, i, n)
    return []


def printMaxActivities(s, f):
    n = len(f)
    print("The following activities are selected")
    i = 0
    print(i)
    for j in range(n):
        if s[j] >= f[i]:
            print(j)
            i = j


if __name__ == '__main__':
    # s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    # f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    s = [0, 1, 1, 1, 2, 3, 4, 5, 5, 5, 6]
    f = [2, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8]
    v = [3, 4, 4, 4, 4, 2, 4, 4, 4, 4, 3]
    start = time()
    print(recursive(s, f, v, 0, len(s)-1),'time elapsed: ', time() - start)
    # start_1 = time()
    # print([(1, 4)] + big(s, f, 0, len(s)), 'time elapsed: ', time() - start_1)
    # start_2 = time()
    # printMaxActivities(s, f)
    # print('time elapsed: ', time() - start_2)