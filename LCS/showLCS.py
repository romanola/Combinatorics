#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/10/18

from tools import benchmark
import time

@benchmark
def dynamic(a, b):
    m = len(a)
    n = len(b)
    val = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if a[i] == b[j]:
                val[i][j] = val[i-1][j-1] + 1
            else:
                val[i][j] = max(val[i-1][j], val[i][j-1])
    return val


# task 6
def show(m, a, b, i, j):
    if i == 0 or j == 0:
        return [a[0]] if i == 0 else [b[0]]
    elif m[i][j] == m[i-1][j-1] + 1:
        return show(m, a, b, i-1, j-1) + [a[i]]
    elif m[i][j] == m[i-1][j]:
        return show(m, a, b, i-1, j)
    elif m[i][j] == m[i-1][j]:
        return show(m, a, b, i, j-1)


if __name__ == '__main__':
    a = '123143'
    b = '12314324525698'
    start = time.time()
    ans = show(dynamic(a, b), a, b, len(a)-1, len(b)-1)
    print(''.join(ans))
    end = time.time()
    print('time elapsed: ', end - start)
