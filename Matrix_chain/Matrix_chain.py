import time
def benchmark(f):
    """
    Декоратор @benchmark для вычисления времени работы функции f
    """
    def _benchmark(*args, **kw):
        t = time.clock()
        rez = f(*args, **kw)
        t = time.clock() - t
        print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
        return rez
    return _benchmark

@benchmark
def MatrixChainOrder(p, n):

    m = [[-1 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]

    for i in range(1, n):
        m[i][i] = 0

    for length in range(2, n):       # for each chain length
        for i in range(1, n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                # cost = cost/scalar multiplications
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost > m[i][j]:     # find maximum
                    m[i][j] = cost
                    s[i][j] = k        # in addition we remember place, where we did the split

    return m, s


def get_answer(s, i, j, res: list):
    if i == j:
        res.append('a[{}]'.format(i-1))    # on the main diagonal length of piece == 0, so matrix only one
    else:
        res.append('(')                  # at the other places the internal block of matrix opens
        get_answer(s, i, s[i][j], res)
        get_answer(s, s[i][j]+1, j, res)
        res.append(')')


if __name__ == '__main__':

    # test of the above function
    arr = [30, 35, 15, 5, 10, 20, 25, 5, 16, 34, 28, 19, 66, 34, 78, 55, 23]
    size = len(arr)
    res_m, res_s = MatrixChainOrder(arr, size)
    answer = []
    get_answer(res_s, 1, size-1, answer)
    print("Maximum number of multiplications is {}".format(res_m[1][size-1]))

    print("The right sequence is {}".format(answer))