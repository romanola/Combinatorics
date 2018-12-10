#!/usr/bin/env python
# coding: utf-8
# Author: kentyn Kofanov (knu)
# Created: 11/10/18

from tools import benchmark


# task 2
@benchmark
def dynamic(a):
    n = len(a)
    dyn = [1 for _ in range(n)]
    res_array = [-1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if a[j] <= a[i]:
                if 1 + dyn[j] > dyn[i]:
                    dyn[i] = 1 + dyn[j]
                    res_array[i] = j
    pos = -1
    res = 0
    for i, el in enumerate(dyn):
        if el > res:
            res = el
            pos = i

    path = []
    while pos != -1:
        path.append(a[pos])
        pos = res_array[pos]
    return res, ''.join(path[::-1])


if __name__ == '__main__':
    b = '12314324525698'
    ans = dynamic(b)
    print(*ans)
