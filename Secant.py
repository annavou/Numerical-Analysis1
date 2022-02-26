import numpy as np


def f(x):
    return (14 * x * np.exp(x - 2)) - (12 * np.exp(x - 2)) - (7 * pow(x, 3)) + (20 * pow(x, 2)) - (26 * x) + 12


def secant(x0, x1, k):
    print(1, x0)
    print(2, x1)
    i = 3
    e = 1 / 2 * pow(10, -k)
    while True:
        x = x1 - ((f(x1) * (x1 - x0)) / (f(x1) - f(x0)))
        if abs(x - x1) < e:
            break
        x0 = x1
        x1 = x
        print(i, round(x, 5), f(x))
        i = i + 1


secant(0.1, 0.9, 5)
print("\n")
secant(1.5, 2.3, 5)
