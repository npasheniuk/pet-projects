import math


def f(x):
    return math.atan(x) - math.exp(-x)


def relaxation():
    e = 1e-3
    x_0 = 3
    alpha = -1
    x_1 = x_0 + alpha * f(x_0)
    k = 0
    while abs(x_1 - x_0) > e:
        k += 1
        x_0 = x_1
        x_1 = x_0 + alpha * f(x_0)
    print(k)
    return x_1


print(relaxation())
