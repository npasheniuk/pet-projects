def f(x):
    return x**3 - 7*x + 6


def dich():
    a = -3
    b = 3
    e = 1e-4
    res = 0
    while abs(b - a) > e:
        c = (a + b) / 2
        if f(a) * f(c) <= 0:
            b = c
            res = c
        if f(c) * f(b) <= 0:
            a = c
            res = c
        if f(c) == 0:
            res = c
            break
    return res


print(dich())


