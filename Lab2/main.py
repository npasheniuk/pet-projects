"""
[A, B] - range of valid values of x
"""

A = -1
B = 1


def check_x():
    """
    In function check_x() we are checking value x on our range of valid values
    """
    try:
        x_input = input(f'Enter right number x(from {A} to {B}): ')
        x = float(x_input)
    except (EOFError, KeyboardInterrupt, Exception) as e:
        print('***** Error')
        print(f'We catch a problem in your input data: {e}')
        return
    if A <= x <= B:
        return x
    else:
        print('***** Error')
        print('Wrong number x')
        return


def check_eps():
    """
    In function check_eps() we are checking value eps on our range of valid values
    """
    try:
        eps_input = input('Enter right number eps(it must be > 0, but very small): ')
        eps = float(eps_input)
    except (EOFError, KeyboardInterrupt, Exception) as e:
        print('***** Error')
        print(f'We catch a problem in your input data: {e}')
        return
    if eps > 0:
        return eps
    else:
        print('***** Error')
        print('Wrong number eps')
        return


def s(x, eps) -> float:
    """
    In function s() we calculating our example that depends on x and eps
    """
    n = 0
    z = x * x / 2
    sum = z

    while z >= eps or z <= -eps:
        n += 1
        z = z * (-1) * n * n * x * x / ((2 * n + 2) * (2 * n + 1))
        sum += z
    else:
        return sum


def answer():
    """
    In function answer() we calling all other functions and writing answer
    """
    x = check_x()
    if x is None:
        return
    eps = check_eps()
    if eps is None:
        return
    print('***** do calculations ... ', end='')
    result = s(x, eps)
    print(f'done\nfor x = {x:.5f}\nfor eps = {eps:.4e}\nresult = {result:.9f}')


"""
Informing about main direction of program and about human, who did this program
"""
print('This program is going to calculate recursion function that depends on value x, Variant 22')
print('This program made by Nikita Pasheniuk, K-10')
answer()
