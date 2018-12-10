from math import e, sqrt
import numpy as np
from numpy.linalg import inv
import sys


def bisection(a, b, f, epsilon):
    """
    :param a: first value to check in the function
    :param b: second value to check in the function
    :param f: The function to check
    :param epsilon: error tolerance
    :return: m: the root of the function
    """
    m = (a + b) / 2.0
    while abs(a - b) > epsilon:
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
        m = (a + b) / 2.0
    return m


def newton_rapson(func, x=0, it=1, h=0.00000001):
    """
    :param func: the function to get it's roots
    :param x: starting guess(default=0)
    :param it: the maximum number of allowed iterations(default=1)
    :param h: accuracy factor of the method (default=0.00000001)
    :return: An estimated root of the funtion
    """

    def der(f, h):
        return lambda x0: (f(x0 + h) - f(x0)) / h

    if der(func, h)(x) == 0:
        x = 1
    for i in range(it):
        fd = func(x)
        ft = der(func, h)(x)
        x = x - (fd / ft)
    return x


def func(x):
    return x * pow(e, -1 * x) - 0.25


def R(i, j):
    return sqrt(pow(i[0] - j[0], 2) + pow(i[1] - j[1], 2) + pow(200 - 0, 2))


y = newton_rapson(func, 3, it=100)
b = bisection(-1 * y, y, func, 0.0000001)
while b > y:
    y = b
    b = bisection(-1 * y, y, func, 0.0000001)
u = b / 100

D = [[0 for x in range(4)] for y in range(4)]
M = ((50, 50), (50, 150), (150, 50), (150, 150))
c = 0.6129015
k = 3.73621
for i in range(4):
    for j in range(4):
        D[i][j] = (c * (1 + k * 200) * pow(e, -1 * u * R(M[i], M[j]))) / pow(R(M[i], M[j]), 2)
        print("[", D[i][j], "]", end=",")
    print("")

final=np.array(D)
M=(900,950,1000,1100)
print(inv(D).dot(M))
