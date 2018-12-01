#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 01.12.2018

import random
import math

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

def prepare(n):
    """
    Представляє число n у вигляді t*2**s, t = 2*k+1 (нечетно)
    :param n: число, яке переводимо
    :return: (s, t); s - кількість разів піднесення до степеня числа n,
                     t - залишок від ділення числа n на 2 в степені s
    """
    s = 0
    while not n % 2:
        n /= 2
        s += 1
    return s, n

def check(a, s, t, n):
    """
    Допоміжна функція перевірки на простоту для окремого свідка простоти a
    :param a: свідок простоти
    :param s: степінь, у який підносимо свідка простоти а для представлення числа n
    :param t: залишок від ділення числа n на 2 в степені s
    :param n: число, яке перевіряємо на простоту
    :return: True - псевдопросте , False - складене
    """
    x = pow(a, t, n)
    if x == 1:
        return True
    for i in range(s - 1):
        if x == n - 1:
            return True
        x = pow(x, 2, n)
    return x == n - 1

def sieveOfEratosthenes(n):
    """
    Допоміжна функція "Решето Ератосфена"для перевірки на простоту
    :param n: число, яке перевіряємо на простоту
    :return: True - якщо число n - просте, False - якщо n складене
    """
    succees = True
    for i in range(1, int(math.sqrt(n))+1):
        if not is_prime(i, n):
            succees = False
            break
    return succees


def CarmichaelCheck(n):
    """
    Перевірка числа на число Кармайкла
    :param n: число
    :return: True/False
    """
    def _helpCheck(b, n):
        """тест Ферма"""
        return pow(b, n-1, n) == 1  # повертає b**(n-1) = 1 (mod n)
    if sieveOfEratosthenes(n):
        return False
    success = True
    for i in range(1, n):
        if is_prime(i, n) and not _helpCheck(i, n):
            success = False
            break
    return success

def MillerRabin(n, k=50):
    """
    Тест на простоту Міллера-Рабіна
    :param n: число для перевірки
    :param k: кількість тестів
    :return: True - вірогідно просте, False - складене
    """
    if n in [1, 2, 3]:
        return True
    if not n & 1:  # перевірка на парність
        return False
    if CarmichaelCheck(n):  # перевірка на число Кармайкла
        return False
    s, t = prepare(n-1)
    for i in range(k):
        a = random.randrange(2, n-1)
        if not check(a, s, int(t), n):
            return False
    return True



if __name__ == '__main__':
    #task1
    n = 25
    for i in range(1, n):
        print(i, fermats_test(i))
    print('\n')
    #task2
    s = 1000
    for i in range(1, s):
        print(i, MillerRabin(i))
