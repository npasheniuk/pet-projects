from scipy.misc import derivative


def f(x):
    return x**3 - 7*x + 6


def newton():
    x = 5
    e = 1e-4
    x_1 = x - f(x) / derivative(f, x)
    while abs(x_1 - x) > e:
        x = x_1
        x_1 = x - f(x) / derivative(f, x)
    return x_1


print(newton())
