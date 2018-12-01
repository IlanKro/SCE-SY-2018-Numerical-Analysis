import sys
def bisection(a, b,f, epsilon):
    """
    :param a: first value to check in the function
    :param b: second value to check in the function
    :param f: The function to check
    :param epsilon: error tolerance
    :return: m: the root of the function
    """
    m = (a + b) / 2.0
    while abs(a - b) > epsilon:
        if f(m) == 0:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
        m = (a + b) / 2.0
    return m
