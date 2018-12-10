#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/10/18
from tools import memo
import time


# task 1
@memo
def recursive(a, i, j):
    if i == j:
        return 1, (a[i], )
    pc, ps = recursive(a, i-1, j)
    if a[i] >= ps[-1]:
        return pc + 1, ps + (a[i], )
    else:
        mc = 1
        ms = (a[i],)
        for k in range(j, i):
            tmp, tmp_seq = recursive(a, i-1, k)
            if tmp+1 > mc and a[i] >= tmp_seq[-1]:
                mc = tmp + 1
                ms = tmp_seq + (a[i], )
        for k in range(i):
            tmp, tmp_seq = recursive(a, k, 0)
            if tmp+1 > mc and a[i] >= tmp_seq[-1]:
                mc = tmp + 1
                ms = tmp_seq + (a[i], )
        return (mc, ms) if mc > pc else (pc, ps)


if __name__ == '__main__':
    start = time.time()
    b = '12314324525698'
    ans = recursive(b, len(b)-1, 0)
    end = time.time()
    print(ans[0], ''.join(ans[1]))
    print('time elapsed: ', end - start)