import numpy as np


def f(x):
    return (14 * x * np.exp(x - 2)) - (12 * np.exp(x - 2)) - (7 * pow(x, 3)) + (20 * pow(x, 2)) - (26 * x) + 12


def bisection(a, b, k):
    if f(a)*f(b)>= 0:
        return

    e = 1 / 2 * pow(10, -k)
    n = (np.log10(b - a) - np.log10(e)) / np.log10(2)

    i = 1
    while i <= n:
        m = (a + b) / 2
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


print("N a  b   m    f(m)")
bisection(0, 1.5, 5)

print("\n")

print("N a   b   m    f(m)")
bisection(1.7, 3, 5)
