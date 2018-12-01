def newton_rapson(func, x=0, it=1, h=0.00000001):
    """
    :param func: the function to get it's roots 
    :param x: starting guess(default=0)
    :param it: the maximum number of allowed iterations(default=1)
    :param h: accuracy factor of the method (default=0.00000001)
    :return: An estimated root of the funtion
    """
    def der(f, h):
        return lambda x0: (f(x0 + h) - f(x0)) / h

    if der(func, h)(x) == 0:
        x = 1
    for i in range(it):
        fd = func(x)
        ft = der(func, h)(x)
        x = x - (fd / ft)
    return x
