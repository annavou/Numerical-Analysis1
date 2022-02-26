import numpy as np


def f(x):
    return (1/x)-8.3


def diff_f(x):
    return -(1/pow(x,2))


def diff2_f(x):
    return 2/pow(x,3)


def newtonraphson(x0, k):
    i = 1
    e = 1 / 2 * pow(10, -k)
    while True:
        x = x0 - (f(x0) / diff_f(x0))
        if i == 1:
            print(i, x0)
        if abs(x - x0) < e:
            break
        x0 = x
        i = i + 1
        print(i, round(x, 5), f(x))
    if diff2_f(round(x, 4)) != 0:
        print("Συγκλίνει τετραγωνικά")
    else:
        print("Δεν συγκλίνει τετραγωνικά")


newtonraphson(0.24, 2)

