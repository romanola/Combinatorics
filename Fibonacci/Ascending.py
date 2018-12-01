#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 01.12.2018

def fibon(n):
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a+b
    return b

