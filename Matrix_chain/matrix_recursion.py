#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 07.12.2018

import time

MIN = -1


def memoized_matrix_chain(p):
    """ Cover for recursive function _lookup_chain
    :param p: array of dimensions of matrix
    :return: array n x n of maximum amount of elementary operations for each pair i, j
             array n x n of right split of matrix chain
    """
    n = len(p) - 1
    m = [[MIN for i in range(0, n+1)] for i in range(0, n+1)]
    s = [[0 for i in range(0, n+1)] for i in range(0, n+1)]
    _lookup_chain(m, s, p, 1, n)
    return m, s


def _lookup_chain(m, s, p, i, j):
    """ Recursive solution of reversed matrix chain problem -
        find the sequence of brackets that gives the biggest number of
        elementary operations for multiplication the chain of matrix
    :param m: array n+1 x n+1 of results of subproblems (cache)
    :param s: array n+1 x n+1 of index of split the chain for rebuild the answer
    :param p: array 1 x n of matrix dimensions
    :param i: start of piece
    :param j: end of piece
    :return: solution of subproblem
    """
    if m[i][j] > MIN:    # if we have already calculated this subproblem
        return m[i][j]   # return the calculated result
    if i == j:
        m[i][j] = 0      # on the main diagonal length of chain piece == 1 so we don't need to multiply
    else:
        for k in range(i, j):
            q = _lookup_chain(m, s, p, i, k) + _lookup_chain(m, s, p, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q > m[i][j]:
                m[i][j] = q
                s[i][j] = k        # in addition remember the index of splitting
    return m[i][j]


def get_answer(s, i, j, res: list):
    """ Reconstruct the sequence of brackets and matrix
        that give the maximum number of operations
    :param s: array n x n of right split of matrix chain from MatrixChainOrder
    :param i: start of piece
    :param j: end of piece
    :param res: array of string from set {'(', ')', 'a[i]'}
    :return: None (array changes inside of function)
    """
    if i == j:
        res.append('a[{}]'.format(i-1))    # on the main diagonal length of piece == 0, so matrix only one
    else:
        res.append('(')                  # at the other places the internal block of matrix opens
        get_answer(s, i, s[i][j], res)
        get_answer(s, s[i][j]+1, j, res)
        res.append(')')


def main():
    p = [30, 35, 15, 5, 10, 20, 25, 5, 16, 34, 28, 19, 66, 34, 78, 55, 23]
    size = len(p)
    res_m, s = memoized_matrix_chain(p)
    answer = []
    get_answer(s, 1, size-1, answer)

    print("Maximum number of multiplications is {}".format(res_m[1][size - 1]))

    print("The right sequence is {}".format(answer))


if __name__ == '__main__':
    b = time.time()
    main()
    print('total run time is:', time.time() - b)