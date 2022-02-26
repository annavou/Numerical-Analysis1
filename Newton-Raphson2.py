import numpy as np


def f(x):
    return (54 * pow(x, 6)) + (45 * pow(x, 5)) - (102 * pow(x, 4)) - (69 * pow(x, 3)) + (35 * pow(x, 2)) + (16 * x) - 4


def df(x):
    return (324 * pow(x, 5)) + (225 * pow(x, 4)) - (408 * pow(x, 3)) - (207 * pow(x, 2)) + (70 * x) + 16


def ddf(x):
    return (1620 * pow(x, 4)) + (900 * pow(x, 3)) - (1224 * pow(x, 2)) - (414 * x) + 70


def newtonraphson(x0, k):
    i = 1
    e = 1 / 2 * pow(10, -k)
    while True:
        x = x0 - (1 / ((df(x0) / f(x0)) - ((1 / 2) * (ddf(x0) / df(x0)))))
        if i == 1:
            print(i, x0)
        if abs(x - x0) < e:
            break
        x0 = x
        i = i + 1
        print(i, round(x, 5), f(x))


newtonraphson(-2, 5)
print("\n")
newtonraphson(-1, 5)
print("\n")
newtonraphson(0, 5)
print("\n")
newtonraphson(0.4, 5)
print("\n")
newtonraphson(1, 5)
print("\n")
