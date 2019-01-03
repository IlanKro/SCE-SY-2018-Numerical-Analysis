def trapezium(f=lambda x:x,a=0,b=1,n=1000):
    """
    Calculates and prints the process of trapezium method for calculating an integral
    :param f: the function to calculate its' integral
    :param a: the initial value to calculate the integral from
    :param b: the end value of the integral
    :param n: the amount of parts to calculate the integral
    :return: the calculation of the integral
    """
    def delta_x(a, b, n):
        return (b - a) / n
    integral=f(a)
    h=delta_x(a,b,n)
    print('{}/2 * ({}'.format(h,integral), end="")
    multiplier=2
    for i in range(1,n-1):
        fxi= multiplier*f(a+i*h)
        print (" + {}*{} ".format(multiplier,fxi),end="")
        integral+=fxi

    print("+ {})".format(f(b)))
    return (h/2) * (integral + f(b))

print(trapezium(lambda x:x**3,0,1,10000))
