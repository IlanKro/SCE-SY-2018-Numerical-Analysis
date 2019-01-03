def newton_rapson(func, x=0, it=10, h=0.00000001):
    """
    :param func: the function to get it's roots 
    :param x: starting guess(default=0)
    :param it: the number of iterations(default=10)
    :param h: accuracy factor of the method (default=0.00000001)
    :return: An estimated root of the funtion
    """
    print("initial guess: {}".format(x))
    def der(f, h):
        print ("f(x0+{0})-f(x0)/{0}".format(h))
        return lambda x0: (f(x0 + h) - f(x0)) / h

    if der(func, h)(x) == 0:
        x = 1
    for i in range(it):
        fd = func(x)
        ft = der(func, h)(x)
        x = x - (fd / ft)
        print ("{})guess={}".format(i+1,x))

    return x

print (newton_rapson(lambda x: pow(x,3) - 3*(x**2)+ x +1,3,10,0.00001))
