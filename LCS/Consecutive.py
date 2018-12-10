#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/10/18

from tools import benchmark


# task 3-4
@benchmark
def dynamic(a, b):
    m = len(a)
    n = len(b)
    d = [[0 for _ in range(n)] for _ in range(m)]
    prev = [-1 for _ in range(n)]
    gm = 0
    gp = -1
    for i in range(0, m):
        for j in range(0, n):
            if a[i] == b[j]:
                ml = 0
                mp = -1
                for k in range(i+1):
                    for l in range(j+1):
                        if k == i and l == j:
                            continue
                        if d[k][l] > ml and a[k] == b[l] == a[i] - 1:
                            ml = d[k][l]
                            mp = l
                d[i][j] = ml + 1
                if d[i][j] > gm:
                    gm = d[i][j]
                    gp = j
                prev[j] = mp
    res = []
    while gp != -1:
        res.append(b[gp])
        gp = prev[gp]
    return res[::-1]


if __name__ == '__main__':
    a = '8319874197398402701940375814'
    b = '37847072388529835342983'
    ans = dynamic(tuple(map(int, a)), tuple(map(int, b)))
    print(''.join(map(str, ans)))
