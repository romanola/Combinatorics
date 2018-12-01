#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 01.12.2018

import random
def gcd_is(m,n):
    """
    Найбільший спільний дільник двох чисел
    :param m: перше число
    :param n: друге число
    :return: gcd(m, n)
    """
    while m != n: # якщо m i n рівні, то ми знайшли найбільший спільний дільник
        if n >= m:
            n -= m
        else:
            m -= n
    return m

def is_prime(m,n):
    """
    Перевірка на взаємну простоту двох чисел
    :param m: перше число
    :param n: друге число
    :return: True - числа взаємно прості, False - числа не взаємно прості
    """
    return gcd_is(m, n) == 1


def fermats_test(n, k = 50):
    """
    Перевірка простоти натурального числа n
    :param n: число для перевірки
    :param k: кількість тестів
    :return: True - якщо n просте, False - якщо n складене
    """
    tmp = True
    for _ in range(k):
        a = n # взаємно просте число з n
        while not is_prime(a,n): # якщо а не взаємно просте з n
            a = random.randint(1, 1000) #знаходимо таке а взаємно просте з n
        if not pow(a, n-1, n) == 1:
            tmp = False
            break

    return tmp

if __name__ == '__main__':
    n = 25
    for i in range(1, n):
        print(i, fermats_test(i))
