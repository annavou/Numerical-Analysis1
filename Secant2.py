import numpy as np


def f(x):
    return (54 * pow(x, 6)) + (45 * pow(x, 5)) - (102 * pow(x, 4)) - (69 * pow(x, 3)) + (35 * pow(x, 2)) + (16 * x) - 4


def df(x):
    return (324 * pow(x, 5)) + (225 * pow(x, 4)) - (408 * pow(x, 3)) - (207 * pow(x, 2)) + (70 * x) + 16


def ddf(x):
    return (1620 * pow(x, 4)) + (900 * pow(x, 3)) - (1224 * pow(x, 2)) - (414 * x) + 70


def secant(x0, x1, x2, k):
    print(1, x0)
    print(2, x1)
    print(3, x2)
    i = 4
    e = 1 / 2 * pow(10, -k)
    while True:
        if f(x1) != 0:
            q = f(x0) / f(x1)
            r = f(x2) / f(x1)
        if f(x0):
            s = f(x2) / f(x0)
        x = x2 - (((r * (r - q) * (x2 - x1)) + ((1 - r) * s * (x2 - x0))) / ((q - 1) * (r - 1) * (s - 1)))
        if abs(x - x1) < e:
            break
        x0 = x1
        x1 = x2
        x2 = x
        print(i, round(x, 5), f(x))
        i = i + 1


secant(-2, -1.8, -1.5, 5)
print("\n")
secant(-1, -0.9, -0.4, 5)
print("\n")
secant(0, 0.1, 0.3, 5)
print("\n")
secant(0, 0.1, 0.5, 5)
print("\n")
secant(1, 1.1, 2, 5)
