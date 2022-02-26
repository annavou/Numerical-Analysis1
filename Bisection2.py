import numpy as np
import random


def f(x):
    return (54 * pow(x, 6)) + (45 * pow(x, 5)) - (102 * pow(x, 4)) - (69 * pow(x, 3)) + (35 * pow(x, 2)) + (16 * x) - 4


def df(x):
    return (324 * pow(x, 5)) + (225 * pow(x, 4)) - (408 * pow(x, 3)) - (207 * pow(x, 2)) + (70 * x) + 16


def ddf(x):
    return (1620 * pow(x, 4)) + (900 * pow(x, 3)) - (1224 * pow(x, 2)) - (414 * x) + 70


def bisection(a, b, k):
    if f(a) * f(b) >= 0:
        return

    e = 1 / 2 * pow(10, -k)
    n = (np.log10(b - a) - np.log10(e)) / np.log10(2)

    i = 1
    while i <= n:
        m = random.uniform(a, b)
        if f(m) == 0:
            break
        if i == 1:
            print(i, a, b, m, f(m))
        if f(a) * f(m) > 0:
            a = m
        else:
            b = m
        i = i + 1
        print(i, a, b, round(m, 5), f(m))


bisection(-2, -1, 5)
print("\n")
bisection(-1, -0.6, 5)
print("\n")
bisection(0, 0.3, 5)
print("\n")
bisection(0.4, 0.6, 5)
print("\n")
bisection(1, 1.5, 5)
print("\n")
