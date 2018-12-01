#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 01.12.2018
import time

def fibon(n):
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a+b
    return b


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
